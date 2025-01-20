# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [PEP 440](https://www.python.org/dev/peps/pep-0440/) 
and uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.3]
### Changed
- Upgrade to `ASFHyP3/actions` v0.15.0 in cookiecutter workflows.
- Update `mypy` options in `pyproject.toml`.

### Fixed
- Use `TOOLS_BOT_PAK` as recommended by the https://github.com/ASFHyP3/actions README.

## [0.3.2]
### Changed
- The [`static-analysis`]({{cookiecutter.__project_name}}/.github/workflows/static-analysis.yml) Github Actions workflow now includes `mypy` for type checking.

## [0.3.1]
### Changed
- The [`static-analysis`]({{cookiecutter.__project_name}}/.github/workflows/static-analysis.yml) Github Actions workflow now uses `ruff` rather than `flake8` for linting.

## [0.3.0]
### Added
* Support for Python 3.13
* Workflow action to keep the reusable CI/CD action up to date within the cookiecutter template

### Changed
* Now uses ruff for linting and formatting instead of flake8

### Removed
* The unused `process.main` function as we don't register it as a console script entrypoint

### Fixed
* Tests using the `script_runner` fixture will no longer raise usage warnings 

## [0.2.0]
### Removed
* Support for Python 3.8 and 3.9 has been dropped. The minimum version is now 3.10.
### Fixed
* Removed the deprecated `jinja2_time.TimeExtension` from the cookiecutter config

## [0.1.3]
### Changed
* Upgraded to `hyp3lib=>3,<4`.

## [0.1.2]
### Fixed
- Typo in the Docker entrypoint command.

## [0.1.1]
### Fixed
- Typo in the `release-checklist-comment.yml` workflow.

## [0.1.0]
### Added
- Initial release of the HyP3 Cookiecutter.
