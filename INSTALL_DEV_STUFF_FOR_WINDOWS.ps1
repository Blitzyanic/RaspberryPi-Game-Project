# Erstellt eine virtuelle Umgebung
python -m venv env

# Aktiviert die virtuelle Umgebung
.\env\Scripts\Activate.ps1

# Installiert die erforderlichen Python-Pakete
pip install pygame RPi.GPIO pcf8591-library
