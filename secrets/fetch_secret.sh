#!/bin/bash

# Directory where secrets are stored
SECRETS_DIR="$HOME/.ssh/secrets"
VAULT_PASSWORD_FILE="$SECRETS_DIR/vault_pass"
ENCRYPTION_CMD="ansible-vault"

# Debugging function (integrated from SkogAI Debugging System)
debug_echo() {
    local level="$1"
    local message="$2"
    local log_file="${SKOGAI_LOG_FILE:-$HOME/.config/skogai/logs/skogai.log}"
    local debug_level="${SKOGAI_DEBUG_LEVEL:-INFO}"

    # Log levels priority
    declare -A levels=(["LOG"]=0 ["ERROR"]=1 ["WARN"]=2 ["INFO"]=3 ["DEBUG"]=4)

    # Determine if the message should be logged/shown
    if [[ ${levels[$level]} -le ${levels[$debug_level]} ]]; then
        echo "[$level] $message" >&2  # Write to stderr
    fi

    # Always log to file
    mkdir -p "$(dirname "$log_file")"
    echo "$(date '+%Y-%m-%d %H:%M:%S') [$level] $message" >> "$log_file"
}

# Function: is_encrypted
is_encrypted() {
    local file="$1"
    debug_echo "DEBUG" "Checking if file is encrypted: $file"
    $ENCRYPTION_CMD view --vault-password-file "$VAULT_PASSWORD_FILE" "$file" > /dev/null 2>&1
}

# Usage: fetch_secret <secret_name>
SECRET_NAME="$1"

if [[ -z "$SECRET_NAME" ]]; then
    debug_echo "ERROR" "Usage: fetch_secret <secret_name>"
    exit 1
fi

SECRET_FILE="$SECRETS_DIR/$SECRET_NAME"
if [[ ! -f "$SECRET_FILE" ]]; then
    debug_echo "ERROR" "Secret $SECRET_NAME not found in $SECRETS_DIR"
    exit 1
fi

if is_encrypted "$SECRET_FILE"; then
    debug_echo "INFO" "Decrypting secret: $SECRET_NAME"
    $ENCRYPTION_CMD decrypt --vault-password-file "$VAULT_PASSWORD_FILE" "$SECRET_FILE" --output -
else
    debug_echo "INFO" "Fetching plaintext secret: $SECRET_NAME"
    cat "$SECRET_FILE"
fi

