# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

<!-- example
## [1.1.1] - 2021-06-26

### Modified

- `YoloAIO.vpy`: Rework of step 1 for readability and bugfix (see below); Thinner white padding for text box; Added coordinates to simplify maintaining code that crops stuff. Default 'step' is now 1 (duh).

- `YoloAIO.py`: Added to double quote normalization.

### Bugfix

- `YoloAIO.vpy`: In step 1, text box had incorrect vertical position. Also, solved some "Error: __ must be MOD2" issues and an AssertionError in step 3 when looking for 1 Color only.

- `YoloAIO.py`: Reworked CLI UI to behave more intuitively.
-->

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