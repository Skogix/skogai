#!/bin/bash

# Directory where secrets are stored
SECRETS_DIR="$HOME/.ssh/secrets"
ENCRYPTION_CMD="ansible-vault"

# Function: is_encrypted
is_encrypted() {
    local file="$1"
    $ENCRYPTION_CMD view "$file" > /dev/null 2>&1
}

# Usage: encrypt_secret <secret_name> [<secret_value>]
SECRET_NAME="$1"
SECRET_VALUE="$2"

if [[ -z "$SECRET_NAME" ]]; then
    echo "Usage: encrypt_secret <secret_name> [<secret_value>]" >&2
    exit 1
fi

SECRET_FILE="$SECRETS_DIR/$SECRET_NAME"

# Ensure the secrets directory exists
mkdir -p "$SECRETS_DIR"
chmod 700 "$SECRETS_DIR"

if [[ -f "$SECRET_FILE" ]]; then
    if is_encrypted "$SECRET_FILE"; then
        echo "File $SECRET_NAME is already encrypted. Re-encrypting..."
        SECRET_VALUE=$($ENCRYPTION_CMD decrypt "$SECRET_FILE" --output -)
    else
        echo "File $SECRET_NAME exists but is not encrypted. Encrypting it now..."
        SECRET_VALUE=$(cat "$SECRET_FILE")
    fi
fi

if [[ -z "$SECRET_VALUE" ]]; then
    if [[ -z "$2" ]]; then
        echo "Error: Secret value must be provided for new secrets." >&2
        exit 1
    fi
    SECRET_VALUE="$2"
fi

# Encrypt the secret
echo "$SECRET_VALUE" | $ENCRYPTION_CMD encrypt --output "$SECRET_FILE" -
chmod 600 "$SECRET_FILE"
echo "Secret $SECRET_NAME encrypted and stored at $SECRET_FILE"

