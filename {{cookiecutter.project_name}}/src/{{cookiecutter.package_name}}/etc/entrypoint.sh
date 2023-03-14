#!/bin/bash --login
set -e
conda activate {{cookiecutter.project_name}}
exec python -um {{cookiecutter.package_name}} "$@"
