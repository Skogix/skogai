#!/bin/bash

# Create a temporary directory
mkdir -p "$HOME/tmp"

# Change to the temporary directory
cd "$HOME/tmp" || exit

# Install prerequisites
sudo pacman -Sy --needed --noconfirm base-devel git

# Clone paru repository
git clone https://aur.archlinux.org/paru.git

# Change to the paru directory
cd paru || exit

# Build and install paru
makepkg -si --noconfirm

# Clean up
cd "$HOME"
rm -rf "$HOME/tmp/paru"

echo "Paru has been installed successfully!"

