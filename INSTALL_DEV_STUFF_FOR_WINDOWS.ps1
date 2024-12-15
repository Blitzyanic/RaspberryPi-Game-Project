# Creates a virtual environment
python -m venv env

# Activates the virtual environment
.\env\Scripts\Activate.ps1

# Installs the required Python packages
pip install pygame RPi.GPIO gpiod smbus

Write-Host "`n" -NoNewline
Write-Host "Finish installation" -ForegroundColor Green

Write-Host "`n" -NoNewline
Write-Host "run the following command: " -ForegroundColor Blue
Write-Host "source env\bin\activate.ps1" -ForegroundColor White
