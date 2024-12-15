#!/usr/bin/bash

# Creates a virtual environment
virtualenv env

# Activates the virtual environment
source env/bin/activate

# Installs the required Python packages
pip install pygame RPi.GPIO gpiod smbus


echo -e "\n\\x1b[1;32m Finish installation \\e[0m"
echo -e "\e[1;31m run the following commands based on your current shell \e[0m\n"
echo -e "\\x1b[1;34m ZSH or Bash: \\e[0m source env/bin/activate"
echo -e "\\x1b[1;34m Fish: \\e[0m source env/bin/activate.fish"
