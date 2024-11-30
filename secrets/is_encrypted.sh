# Function: is_encrypted
# Checks if a file is an Ansible Vault encrypted file
# Usage: is_encrypted <file_path>
is_encrypted() {
    local file="$1"
    ansible-vault view "$file" > /dev/null 2>&1
}

