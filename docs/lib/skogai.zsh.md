# skogai.zsh

This script is a Zsh utility designed to load configuration modules and handle logging with different levels of verbosity. It provides two main functions: `load_modules` and `debug_echo`.

## Functions

### load_modules

- **Purpose**: Loads configuration files from a specified directory.
- **How it works**: 
  - It checks if the specified directory exists.
  - It iterates over files with extensions `.conf`, `.sh`, `.zsh`, and `.env`.
  - For `.env` files, it exports the variables.
  - For other files, it sources them.
  - It uses `nullglob` to handle cases where no files match the pattern.

### log_to_file

- **Purpose**: Logs messages to a specified file.
- **How it works**: 
  - Ensures the log directory exists and creates it if necessary.
  - Creates the log file if it doesn't exist.
  - Appends messages with a timestamp to the log file.

### debug_echo

- **Purpose**: Outputs debug messages based on the current debug level.
- **How it works**: 
  - Compares the message level with the current debug level.
  - Logs all messages to a file.
  - Prints messages to the console if the message level is above `LOG`.

## Environment Variables

- `SKOGAI_DEBUG_LEVEL`: Sets the verbosity level for debugging messages. Default is `INFO`.
- `SKOGAI_LOG_FILE`: Specifies the path to the log file.

## Usage

To use this script, source it in your Zsh environment and call the functions as needed. Ensure that the `SKOGAI_LOG_FILE` environment variable is set to direct logs to the desired location.
