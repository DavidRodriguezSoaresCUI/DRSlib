# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.7.1] - 23.04.2023

### Added

- `dict_utils`: Collection of operations on `dict`
- `list_utils`: Collection of operations on `list`; moved `flatten_list` from utils
- `hash`: Added method `get_temporary_dir_name`

### Modified

- `utils.caller_info`: small fix for when `frame.code_context` is None

## [0.7.0] - 2023-04-22

### Added

- Augmented type hints
- A few new methods, like `utils.assertTrue`
- Using Mypy, Bandit, Pylint and Flake8 for static code analysis
- Using Black formatter for consistent formatting

### BugFix

- Many fixes linked to usage of static code analysis

## [0.6.dev1] - 2022-06-17

### Added

- `DRSlib.__init__.py`: Added `__all__` to try combatting failed imports.
- `DRSlib.decorators`: Added `minimum_duration`

### BugFix

- `DRSlib.mediainfo.MediaInfo`: fixed not recognizing empty/error value

## [0.5] - 2021-11-15

### Modified

- `DRSlib.mediainfo.MediaInfo`: added warnings when MediaInfo call returns no data.

## [0.5.dev9] - 2021-11-14

### Modified

- `DRSlib.fsdb.get_snapshot_file`: tentative bugfix; truncating snapshot filename to 240 characters to avoid `OSError` on path use.

## [0.5.dev7] - 2021-11-14

### License

- Changed from `the Unlicense` to `CC0 1.0 Universal` after reading [this post](https://softwareengineering.stackexchange.com/a/147120)
    * `LICENSE`: replaced contents with `CC0 1.0 Universal`
- Bugfix: license was registered as `MIT` in `setup.cfg`

### Modified

 - `setup.cfg`: `classifiers` was entirely rewritten

## [0.5.dev5] - 2021-11-14

### Modified

- `DRSlib.utils.LOG_FORMAT`: replaced `name` by `funcName` to reduce log message length
- `README`: New section "Warning to users", plus rearranging sections and correcting semantic

## [0.5.dev4] - 2021-11-14

### Modified

- Moved requirements to `setup.cfg`.
- Documentation: `conf.py` now imports version from `setup.cfg`.

## [0.5.dev3] - 2021-11-14

### BugFix

- `DRSlib.path_tools.replace_file`: tentative bugfix

## [0.5.dev2] - 2021-11-14

### BugFix

- Added requirement `send2trash` plus documentation about it.

## [0.5.dev1] - 2021-11-14

### Added

- `DRSlib.path_tools`: Added `replace_file, open_folder_in_explorer` function.

## [0.4] - 2021-11-14

### Added

- `DRSlib.path_tools`: Added `safe_file_copy` function.

### Bugfix

- `DRSlib.mediainfo.MediaInfo.UNIT_FACTOR`: Added 'b/s' entry
- `DRSlib.path_tools`: try-except block for `win32api` module import; It was causing issues on non-windows installs.

### Documentation

- Refinements/bugfixes to scripts
- Added sections in `usage.rst` about requirements and building documentation.

## [0.4.dev9] - 2021-11-09

### Modified

- `DRSlib.cli_ui.user_input`: Removed debugging code

## [0.4.dev8] - 2021-11-09

### Added

- `DRSlib.utils.LOG_FORMAT`: Format for loggers

### Modified

- `DRSlib.cli_ui.user_input`: Removed debugging code

## [0.4.dev7] - 2021-11-09

### Bugfix

- `DRSlib.mediainfo.MediaInfo.get_datapoint`: return value should be a value

## [0.4.dev6] - 2021-11-09

### Bugfix

- `DRSlib.utils.is_iterable`: bugfix attempt
- `DRSlib.path_tools.FileCollector.collect`: reverted bugfix attempt because there was no bug there

## [0.4.dev5] - 2021-11-09

### Bugfix

- `DRSlib.path_tools.FileCollector.collect` and `DRSlib.path_tools.file_collector`: bugfix attempt

## [0.4.dev4] - 2021-11-09

### Mofified

- `requirements`: fixed version `pywin32=300` because version 302 had issues.

### Bugfix

- `DRSlib.cli_ui.user_input`: bugfix attempt

## [0.4.dev3] - 2021-11-09

### Added

- `requirements`: Added forgotten pywin32 requirement

### Modified

- `DRSlib.cli_ui.user_input`: groundwork for more debugging, plus smart prompt reformat

## [0.4.dev2] - 2021-11-09

### Added

- `DRSlib.mediainfo.MediaInfo.DATAPOINTS`: Added datapoint shorthands

### Modified

- `DRSlib.cli_ui.user_input`: error/exception messages

### Bugfix

- `DRSlib.cli_ui.user_input`

## [0.4.dev1] - 2021-11-09

### Added

- `DRSlib.decorators`: Added `call_progress`

### Modified

- `DRSlib.debug`: Module docstring cleanup.

## [0.3] - 2021-11-08

### Added

- `DRSlib.utils`: Added `is_iterable`, `type_assert`
- `DRSlib`: Added submodules `hash`, `mediainfo`

## [0.2] - 2021-11-08

### Added

- `Changelog`: this file
- `docs`: Sphinx documentation
- `DRSlib.utils`: New submodule
- `DRSlib.cli_ui`: Added `pause`, `yes_or_no`, `cli_explorer`, `clear_screen`, `skipNlines`
- `DRSlib.fsdb`: Added `get_snapshot_file`, `get_folder_snapshot`, `ensure_dir_exists`, `folder_get_file_count`, `folder_get_subdirs`, `windows_list_logical_drives`

### Modified

- `DRSlib.*`: Slight docstring adaptations to fit Sphinx reStructuredText format.
- `requirements.txt`: Added sphinx requirements (+theme)

### Bugfix

- `DRSlib.cli_ui.user_input`: Reworked how user input is tested with `accepted`, as it wasn't working as expected.
- `DRSlib.path_tools`: Renamed module docstring title.

## [0.1.dev2] - 2021-11-05

### Added

- `path_tools`: Added `make_FS_safe`, `find_available_path`, `make_valid_path`

## [0.1.dev1] - 2021-10-31

### Meta

- For technical reasons, a new versioning scheme was adopted and this is the new initial release. Note: this release is built upon "old versioning scheme" v0.2a1

### Bugfix

- `DRSlib.banner.bannerize`: Slight signature edit.

- `DRSlib.path_tools.file_collector`: Modification of how `pattern` is processed.

## [0.1] - 2021-10-31

__INITIAL RELEASE__