#!/bin/bash

# Directory where secrets are stored
SECRETS_DIR="$HOME/.ssh/secrets"
ENCRYPTION_CMD="ansible-vault"

# Function: is_encrypted
is_encrypted() {
    local file="$1"
    $ENCRYPTION_CMD view "$file" > /dev/null 2>&1
}

# Usage: encrypt_vault
if [[ ! -d "$SECRETS_DIR" ]]; then
    echo "Error: Secrets directory $SECRETS_DIR does not exist." >&2
    exit 1
fi

echo "Encrypting all plaintext files in $SECRETS_DIR..."
for file in "$SECRETS_DIR"/*; do
    if [[ -f "$file" ]]; then
        if is_encrypted "$file"; then
            echo "$file is already encrypted. Skipping..."
        else
            echo "Encrypting $file..."
            content=$(cat "$file")
            echo "$content" | $ENCRYPTION_CMD encrypt --output "$file" -
            chmod 600 "$file"
            echo "$file encrypted."
        fi
    fi
done

echo "All plaintext files in $SECRETS_DIR have been processed."

