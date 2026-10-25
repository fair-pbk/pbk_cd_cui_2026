import argparse
import glob
import os
import logging
import shutil
import subprocess
from urllib.parse import urlparse
from urllib.request import urlopen

import yaml

from sbmlpbkutils import run_config, load_config, plot_simulation_results

CONFIGS_PATH = './validation/scenarios/'
OUTPUT_PATH = './validation/outputs/'
REFERENCE_SCENARIOS_PATH = './validation/reference_scenarios.yaml'
VALIDATION_REFERENCES_PATH = './validation/validation_references.yaml'

def load_reference_scenarios(filename=REFERENCE_SCENARIOS_PATH):
    """Load the list of reference scenarios from a YAML file."""
    if (os.path.exists(filename)):
        with open(filename, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data['reference_scenarios']

def retrieve_validation_references(
    path=VALIDATION_REFERENCES_PATH,
    force_recompute=False,
    logger=None
):
    """Download the reference models listed in the validation references YAML file."""
    logger = logger or logging.getLogger('run_validation')
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    for reference in data.get('reference_models', []):
        target_dir = reference['target_path']
        download_file(reference['id'], reference['url'], target_dir, force_recompute, logger)
        for parametrisation in reference.get('parametrisations') or []:
            download_file(
                f"{reference['id']}/{parametrisation['id']}",
                parametrisation['url'],
                target_dir,
                force_recompute,
                logger
            )

def download_file(name, url, target_dir, force_recompute, logger):
    """Download a file into target_dir unless it already exists."""
    target_file = os.path.join(target_dir, os.path.basename(urlparse(url).path))
    if os.path.exists(target_file) and not force_recompute:
        logger.info("Skipping [%s]: already available", name)
        return
    logger.info("Retrieving [%s] from %s", name, url)
    os.makedirs(target_dir, exist_ok=True)
    with urlopen(url, timeout=60) as response, open(target_file, 'wb') as out:
        shutil.copyfileobj(response, out)

def run_validation(configs, force_recompute, skip_r):
    # Configure logger for formatted console output
    logger = logging.getLogger('run_validation')
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
    if not logger.handlers:
        logger.addHandler(console_handler)

    # Ensure output path
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    # Retrieve validation reference models
    retrieve_validation_references(force_recompute=force_recompute, logger=logger)

    # Run R validaton scenarios
    if not skip_r:
        reference_scenarios = load_reference_scenarios()
        if reference_scenarios:
            run_r_validation_scenarios(reference_scenarios, force_recompute, logger)

    # Glob scenario configs and run them
    for file in configs:
        file_dir = os.path.dirname(file)

        # Load config
        config = load_config(file)

        # Create output directory if it does not exist
        out_path = os.path.join(OUTPUT_PATH, os.path.relpath(file_dir, CONFIGS_PATH), config.id)

        # If force recompute then remove output
        if os.path.exists(out_path) and force_recompute:
            shutil.rmtree(out_path)

        # Ensure config output path
        os.makedirs(out_path, exist_ok=True)

        # Run simulations
        logger.info("Running simulation config %s", file)
        run_config(
            config = config,
            out_path = out_path,
            force_recompute = force_recompute,
            logger = logger
        )

        num_outputs = max(len(scenario.outputs) for scenario in config.scenarios)

        # Run simulations
        plot_simulation_results(
            config = config,
            out_path = out_path,
            combine_outputs = num_outputs > 1,
            ncols_combined = min(3, num_outputs)
        )

def run_r_validation_scenarios(
    reference_scenarios: list,
    force_recompute: bool,
    logger: logging.Logger
):
    for r_config in reference_scenarios:
        output_file = r_config['output_file']
        if not force_recompute and os.path.exists(output_file):
            logger.info(f"Skipping R config [{r_config['id']}]: results already available")
            continue

        # Run R validation scenarios
        logger.info(f"Running R validation scenario [{r_config['id']}]")
        subprocess.run(['Rscript', r_config['file_path']], check=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run validation scripts arguments.")
    parser.add_argument(
        '--configs',
        '-c',
        nargs='+',
        default=None,
        help='Specific YAML config file(s) to run. If not specified, all configs in CONFIGS_PATH are used.'
    )
    parser.add_argument(
        '-f',
        '--force_recompute',
        action="store_true",
        default=False,
        help="Force re-calculation of validation results instead of using cached results."
    )
    parser.add_argument(
        '--skip_r',
        action="store_true",
        default=False,
        help="Skip running of R validation scenarios."
    )
    args = parser.parse_args()

    if args.configs:
        configs = args.configs
    else:
        configs = glob.glob(f'./{CONFIGS_PATH}/**/*.yaml', recursive=True)
    force_recompute = args.force_recompute
    skip_r = args.skip_r

    run_validation(configs, force_recompute, skip_r)
