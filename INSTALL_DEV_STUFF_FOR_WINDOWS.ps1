# Creates a virtual environment
python -m venv env

# Activates the virtual environment
.\env\Scripts\Activate.ps1

# Installs the required Python packages
pip install pygame

Write-Host "`n" -NoNewline
Write-Host "Finish installation" -ForegroundColor Green

Write-Host "Note this Project uses more libs then pygame but RPi.GPIO, gpiod, smbus are not usable on Windows" -ForegroundColor Red

Write-Host "`n" -NoNewline
Write-Host "run the following command: " -ForegroundColor Blue
Write-Host ".\env\Scripts\Activate.ps1" -ForegroundColor White
