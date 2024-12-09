#!/bin/zsh

# Navigate to the Skogai home directory
cd "$SKOGAI_HOME" || {
    echo "Error: Unable to navigate to Skogai home directory: $SKOGAI_HOME"
    exit 1
}

# Run direnv allow
direnv allow
