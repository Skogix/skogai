#!/bin/zsh

# Check if paru or yay is installed
if command -v paru &> /dev/null; then
    installer="paru"
elif command -v yay &> /dev/null; then
    installer="yay"
else
    echo "Error: Neither paru nor yay is installed. Please install one of them first."
    exit 1
fi

# Install lazygit and dotenv
$installer -S lazygit dotenv
