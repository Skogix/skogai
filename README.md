# SkogAI Project

SkogAI is a modular and AI-driven project to manage an Arch Linux workstation. It leverages small, specialized AI agents to handle system tasks, improve workflows, and streamline workstation management. The system prioritizes modularity, environment-variable-driven configurations, and a `.d`-style structure for dynamic settings. Core functionalities include managing documentation, dotfiles, and system configurations, with the ultimate goal of creating a cohesive and adaptable AI-managed workstation.

## Current Features

### Zsh Configuration Loader
SkogAI includes a robust solution for dynamically loading `.zshrc` configurations from the `.config/zsh.d` directory using the `lib/skogai.zsh` library. This is facilitated by:
- **`load_modules()`**: Loads modular Zsh configuration files.
- **`log_to_file()`**: Logs activity to a file for debugging and monitoring.
- **`debug_echo()`**: Outputs debug information to the terminal based on the current debug level.

### Logging and Debugging
- Logs are maintained in `logs/skogai.log`.
- Debugging output is configurable through the `SKOGAI_DEBUG_LEVEL` environment variable.

### Secrets Management
The `secrets` directory contains shell scripts designed to work with **Ansible** for secure information handling. These scripts facilitate the encryption and decryption of sensitive data:
- **Encryption**: Uses Ansible Vault to securely encrypt files and secrets.
- **Decryption**: Decrypts information with Ansible for use during playbook execution or local management.

Scripts in the `secrets` directory include:
- `encrypt_secret.sh` / `decrypt_secret.sh`: Encrypt or decrypt individual secrets.
- `encrypt_vault.sh` / `decrypt_vault.sh`: Manage Ansible Vault encryption/decryption.
- `fetch_secret.sh`: Retrieve secrets during Ansible operations.
- `is_encrypted.sh`: Verify if a file or secret is encrypted.

### Environment Variables
SkogAI relies on environment variables for flexibility and customization:
```bash
# General Configuration
SKOGAI_HOME=$HOME/skogai
SKOGAI_DEBUG_LEVEL=LOG
```

### File Structure
The project is organized for clarity and modularity:
```
.
├── config
│   ├── user-preferences.md
│   └── zsh.d
│       ├── alias.zsh
│       ├── env.zsh
│       ├── path.zsh
│       ├── prompt.zsh
│       ├── sgpt.zsh
│       └── skogai.env
├── lib
│   └── skogai.zsh
├── logs
│   └── skogai.log
├── README.md
├── secrets
│   ├── decrypt_secret.sh
│   ├── decrypt_vault.sh
│   ├── encrypt_secret.sh
│   ├── encrypt_vault.sh
│   ├── fetch_secret.sh
│   └── is_encrypted.sh
```

## Vision
SkogAI aims to expand into a fully AI-driven manager for:
- **System Customization**: Handling todos, dotfiles, and environment setup.
- **AI-Orchestrated Modules**: Allowing AI-driven creation and integration of new functionalities.
- **Enhanced Workflows**: Leveraging AI to assist with day-to-day system tasks and productivity tools.
