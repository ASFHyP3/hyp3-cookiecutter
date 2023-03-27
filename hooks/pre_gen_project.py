import re
import sys

PROCESS_REGEX = r'^[\-_a-zA-Z0-9]+$'
PROJECT_REGEX = r'^[_a-zA-Z][\-_a-zA-Z0-9]+$'
PACKAGE_REGEX = r'^[_a-z][_a-z0-9]+$'

process_name = '{{ cookiecutter.__process_name }}'
project_name = '{{ cookiecutter.__project_name }}'
package_name = '{{ cookiecutter.__package_name }}'

if not re.match(PROCESS_REGEX, process_name):
    print(f'ERROR: {process_name} is not a valid proccess name!\n'
          f'  Name should match this regex: {PROCESS_REGEX}')
    sys.exit(1)

if not re.match(PROJECT_REGEX, project_name):
    print(f'ERROR: {project_name} is not a valid GitHub project name!\n'
          f'  Name should match this regex: {PROJECT_REGEX}')
    sys.exit(1)

if not re.match(PACKAGE_REGEX, package_name):
    print(f'ERROR: {package_name} is not a valid Python package name!\n'
          f'  See: https://pep8.org/#package-and-module-names')
    sys.exit(1)
