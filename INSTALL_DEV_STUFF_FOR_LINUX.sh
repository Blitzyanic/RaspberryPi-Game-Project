# Creates a virtual environment
virtualenv env

# Activates the virtual eironment
if [ "$SHELL" == "/bin/fish" ]; then
    source env/bin/activate.fish    
else
    source env/bin/activate
fi

# Installs the required Python packages
pip install pygame RPi.GPIO gpiod
