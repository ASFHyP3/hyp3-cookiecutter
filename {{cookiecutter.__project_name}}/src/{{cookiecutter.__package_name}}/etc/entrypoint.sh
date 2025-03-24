#!/bin/bash --login
set -e
conda activate {{ cookiecutter.__project_name }}
exec python -um {{ cookiecutter.__package_name }} "$@"
