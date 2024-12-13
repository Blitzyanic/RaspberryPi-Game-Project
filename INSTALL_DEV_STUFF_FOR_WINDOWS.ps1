# Creates a virtual environment
python -m venv env

# Activates the virtual environment
.\env\Scripts\Activate.ps1

# Installs the required Python packages
pip install pygame RPi.GPIO pcf8591-library
