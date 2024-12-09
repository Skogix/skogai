#!/bin/zsh

# Check if the command is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <command>"
  exit 1
fi

# Run the command with --help and pipe the output to the appropriate help file
command="$1"
help_file="docs/help/${command}.help"

# Execute the command and redirect the output
$command --help > "$help_file"
