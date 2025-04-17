# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [PEP 440](https://www.python.org/dev/peps/pep-0440/) 
and uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.1]

### Added
- Added `permissions` field for every GitHub Actions job in the cookiecutter template, to address https://github.com/ASFHyP3/actions/issues/220

### Changed
- Upgraded `ASFHyP3/actions` reusable actions to `v0.18.1`.

### Fixed
- Updated README instructions for creating a HyP3 plugin. In particular, added instructions for granting the GitHub user account (e.g. `tools-bot` for `ASFHyP3` repos) sufficient permissions for performing releases.
- Changed the value of the `sync_pr_label` parameter for `reusable-release.yml` from `actions-bot` to `{{ cookiecutter.github_username }}` (e.g. `tools-bot` for `ASFHyP3` repos).
- The `python_version` parameter is now provided to `reusable-version-info.yml` in the `test-and-build.yml` template.
- Changed the value of the `user` parameter for `reusable-docker-ghcr.yml` from `{{ cookiecutter.github_username }}` to `{{ '${{ github.actor }}' }}`, to match the example given by the [actions README](https://github.com/ASFHyP3/actions/blob/v0.18.0/README.md#reusable-docker-ghcryml).

## [0.5.0]
### Added
- Added a CLI option to specify the name of a user GitHub Token in the rendered plugin for the GitHub Actions workflows that require it.  
- A GitHub Actions workflow that will ensure hyp3-cookiecutter renders.
### Fixed
- Fixed project name variable error which prevented the cookiecutter from rendering.

## [0.4.0]
### Changed
- In the generated project, ruff and mypy dependencies are now statically pinned and kept up to date with dependabot to prevent updates introducing unexpected static analysis failures  

### Fixed
- Added mypy to the generated Python package's optional `develop` dependencies
- Updates the generated `CHANGELOG.md` to better match the general styles used in HyP3 repositories 
- Ensured the generated Python package passes ruff, mypy, and pytest checks

### Removed
- Removed the broken browse image generation and upload example code
- Removed the generated Code of Conduct file to instead prefer a GitHub organization level one 

## [0.3.3]
### Changed
- Upgrade to `ASFHyP3/actions` v0.15.0 in cookiecutter workflows.
- Update `mypy` options in `pyproject.toml`.

### Fixed
- Use `TOOLS_BOT_PAK` in cookiecutter workflows as recommended by the https://github.com/ASFHyP3/actions README.

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
