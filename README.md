# Skogix AI - Dotfile Management with AI Agents

Welcome to the Skogix AI project! This project aims to revolutionize the way we manage and back up dotfiles by integrating intelligent AI agents to automate and simplify configuration management on Linux systems. By leveraging modular design principles and tools like GNU Stow, the project ensures a seamless, efficient, and user-friendly experience for handling configuration files.

---

## 🚀 Features

- **AI-Powered Backup System**: Automates the backup of dotfiles by detecting changes and ensuring up-to-date configurations.
- **Modular Structure**: Dotfiles and scripts are organized into distinct modules for clarity and maintainability.
- **GNU Stow Integration**: Simplifies the management of symlinks for dotfiles, making installation and updates effortless.
- **Version Control with Git**: Tracks all changes in configuration files to enable easy rollback and collaborative management.
- **Dynamic Task Scheduling**: Uses AI agents to determine optimal backup times based on user activity.
- **Error Handling and Recovery**: Proactively monitors for issues, providing clear feedback and automated fixes when necessary.

---

## 📂 Project Structure

The Skogix AI project is organized into a modular structure, where each module represents a distinct functionality or set of configurations. Here are the main components:

- **`ai/`**: Contains AI agent configurations and scripts for managing and automating tasks.
- **`stow/`**: Configurations and tools for managing symlinks with GNU Stow.
- **`terminal/`**: Dotfiles and settings for terminal and window managers.
- **`bin/`**: Contains all executable scripts used by the AI agents or manually for managing the system.
- **`.help` Files**: Provide concise documentation for key topics like AI usage, Git integration, and command usage.

---

## 🛠️ How It Works

1. **AI Agents**: The AI agents continuously monitor the dotfiles for changes. When updates are detected, the agents automatically:
   - Create backups of the modified files.
   - Update the version control system (Git) to track the changes.
   - Restow the updated files to ensure consistency.

2. **Modular Management**:
   - Each module encapsulates related configurations (e.g., terminal settings, AI tools).
   - GNU Stow is used to symlink these configurations into the appropriate system directories.

3. **Version Control**:
   - All dotfiles and configurations are tracked in Git.
   - When files are added, modified, or deleted, the AI agents handle the Git commands (`git add`, `git rm`) to maintain a clean repository.

4. **Feedback and Logging**:
   - All actions performed by the AI agents are logged with consistent and clear output starting with `[skogix]:`, per project standards.
   - Logs provide transparency and make debugging easy.

---

## 🔧 Getting Started

### Prerequisites

1. **Linux System**: The project is designed for Linux-based operating systems.
2. **GNU Stow**: Install GNU Stow for symlink management:
   ```bash
   sudo pacman -S stow  # For Arch Linux
   ```
3. **Git**: Ensure Git is installed and configured for version control.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Skogix/ai.git
   cd ai
   ```

2. Initialize and update submodules:
   ```bash
   git submodule update --init --recursive
   ```

3. Set up the modules:
   ```bash
   cd stow
   stow [module-name]
   ```

### Usage

- **Run AI Agents**:
   ```bash
   ./bin/ai_backup.sh
   ```

- **Restow Modules**:
   ```bash
   stow [module-name]
   ```

- **Track Changes**:
   ```bash
   git status
   git add [file]
   git commit -m "Updated [module-name] configuration"
   ```

---

## 📖 Documentation

For detailed information on each module or tool, see the `.help` files in the root directory:

- `ai.help`: Information on AI agents.
- `git.help`: Details on Git usage and commands.
- `fzf.help`: Documentation for fuzzy finder integration.

---

## 🛡️ Contribution Guidelines

We welcome contributions! To ensure consistency, follow these guidelines:

1. **File Placement**:
   - Place all executable scripts in the `bin/` folder of the relevant module.
   - Add new modules as top-level directories.

2. **Documentation**:
   - Update `.help` files and ensure any changes to lists or scripts are reflected.

3. **Git Usage**:
   - Always commit changes with clear and descriptive messages.
   - Use `git rm` to remove files properly.

4. **Testing**:
   - Ensure all scripts and AI workflows are tested in a safe environment before committing.

---

## 🤝 Acknowledgments

This project follows the principles outlined in the `rules.md` file, ensuring modularity, maintainability, and user-friendly design. Special thanks to contributors and the open-source community for their support.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
