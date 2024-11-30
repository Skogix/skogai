# Preferences:
1. **Communication Style:**
   - Concise and straight to the point.
   - Avoids unnecessary explanations or "blabbering."
   - Prefers one task, point, or instruction per response.

2. **Workflow and Configurations:**
   - Prefers modular configurations using `.d`-style directories for dynamic management.
   - Generalized loader script for modular configurations located at `$HOME/lib/xyz`.
   - Configuration files should be edited within the home directory, avoiding `/etc/`.
   - Uses Neovim with the Lazy package manager.
   - Prefers receiving install files as one-liners for updating and executing.

3. **System Setup and Tools:**
   - Uses an Arch Linux workstation.
   - SkogAI project focuses on AI-based workstation management.
   - Cloudflare subscription with database options and Zero Trust configuration (not using local `config.yml` for settings).
   - Uses a phone tethered to a computer for internet sharing.

4. **Verification and Validation:**
   - Prefers shell commands for verifying information, which can be copied and executed easily.

---

# SkogAI Project Specifics:
1. The project uses small, specialized AI agents to manage tasks such as:
   - Documentation
   - Dotfiles
   - Git
   - To-dos
   - System configurations
2. Aider will be used as the UI for interaction between the user and AI.
3. The goal is to create a manager AI that orchestrates and standardizes the functionality of smaller agents.
4. Focuses on modularity, dynamic configurations, and environment-variable-driven setups.
5. CrewAI will serve as the foundation for the system, incorporating features inspired by AIChat, Aider, and Open-WebUI.
