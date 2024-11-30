#!/bin/bash

# Directory where secrets are stored
SECRETS_DIR="$HOME/.ssh/secrets"
ENCRYPTION_CMD="ansible-vault decrypt"

# Function: is_encrypted
is_encrypted() {
    local file="$1"
    ansible-vault view "$file" > /dev/null 2>&1
}

# Usage: decrypt_vault
if [[ ! -d "$SECRETS_DIR" ]]; then
    echo "Error: Secrets directory $SECRETS_DIR does not exist." >&2
    exit 1
fi

echo "Decrypting all encrypted files in $SECRETS_DIR..."
for file in "$SECRETS_DIR"/*; do
    if [[ -f "$file" ]]; then
        if is_encrypted "$file"; then
            echo "Decrypting $file..."
            temp_file="${file}.tmp"
            decrypted_content=$($ENCRYPTION_CMD "$file" --output -)
            echo "$decrypted_content" > "$temp_file"
            mv "$temp_file" "$file"
            chmod 600 "$file"
            echo "$file decrypted to plaintext."
        else
            echo "$file is not encrypted. Skipping..."
        fi
    fi
done

