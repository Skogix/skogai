# Setup direnv

To enable `direnv` for your shell, add the following line to your shell configuration file (e.g., `.zshrc` for Zsh):

```shell
eval "$(direnv hook zsh)"
```

This ensures that `direnv` is properly initialized and can manage your environment variables as specified in `.envrc`.
