#!/bin/bash

# Directory where secrets are stored
SECRETS_DIR="$HOME/.ssh/secrets"
ENCRYPTION_CMD="ansible-vault decrypt"

# Function: is_encrypted
is_encrypted() {
    local file="$1"
    ansible-vault view "$file" > /dev/null 2>&1
}

# Usage: decrypt_secret <secret_name>
SECRET_NAME="$1"

if [[ -z "$SECRET_NAME" ]]; then
    echo "Usage: decrypt_secret <secret_name>" >&2
    exit 1
fi

SECRET_FILE="$SECRETS_DIR/$SECRET_NAME"
if [[ ! -f "$SECRET_FILE" ]]; then
    echo "Error: Secret $SECRET_NAME not found in $SECRETS_DIR" >&2
    exit 1
fi

if is_encrypted "$SECRET_FILE"; then
    # Decrypt and display the secret
    $ENCRYPTION_CMD "$SECRET_FILE"
else
    echo "Secret $SECRET_NAME is not encrypted. Outputting plaintext content..."
    cat "$SECRET_FILE"
fi

