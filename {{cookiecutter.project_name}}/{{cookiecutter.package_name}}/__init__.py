"""{{cookiecutter.short_description}}"""

from importlib.metadata import PackageNotFoundError, version

from {{cookiecutter.package_name}}.process import process

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    print('package is not installed!\n'
          'Install in editable/develop mode via (from the top of this repo):\n'
          '   python -m pip install -e .[develop]\n'
          'Or, to just get the version number use:\n'
          '   python setup.py --version')

__all__ = [
    '__version__',
    'process',
]
