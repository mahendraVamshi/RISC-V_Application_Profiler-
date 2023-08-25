from pathlib import Path
import shutil
import click
from riscv_application_profiler import __version__
from riscv_application_profiler.profiler import run
from riscv_application_profiler.isac_port import isac_setup_routine
from riscv_isac.log import logger
import riscv_isac.plugins.spike as isac_spike_plugin
import os
from git import Repo
import yaml  

@click.group()
@click.version_option(version=__version__)
def cli():
    '''Command Line Interface for riscv_application_profiler'''

@cli.command()
# CLI option 'log'.
# Expects an ISA string.
@click.option(
	'-l',
	'--log',
	help=
	'This option expects the path to an execution log.',
	required=True)

# CLI option 'output.
# Expects a directory.
@click.option(
	'-o',
	'--output',
	help="Path to the output file.",
	default='./build',
	show_default=True,
	required=False,
    )

# CLI option 'config'.
# Expects a YAML file.

@click.option('--verbose', '-v', default='info', help='Set verbose level', type=click.Choice(['info','error','debug'],case_sensitive=False))
@click.option('-c', '--config', help="Path to the YAML configuration file.", required=True)
def profile(config, log, output, verbose):
    '''
    Generates the hardware description of the decoder
    '''
    with open(config, 'r') as config_file:
        config_data = yaml.safe_load(config_file)

    isa = config_data['profiles']['cfg']['isa']
    log_file = str(Path(log).absolute())
    output_dir = str(Path(output).absolute())
    isac_setup_routine(lib_dir=f'{output_dir}/lib')

    logger.level(verbose)
    logger.info("**********************************")
    logger.info(f"RISC-V Application Profiler v{__version__}")
    logger.info("**********************************")
    logger.info("ISA Extension used: " + isa)
    
    logger.info(f"\nLog file: {log_file}")
    logger.info(f"Output directory: {output_dir}")

    # Invoke the actual profiler
    run(log_file, isa, output_dir, verbose)
    logger.info("Done profiling.")
    logger.info(f"Reports in {output_dir}/reports.")

def main():
    cli()

if __name__ == '__main__':
    main()