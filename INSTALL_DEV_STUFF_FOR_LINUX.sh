# create venv for libs
virtualenv env

# activate venv for current shell
source env/bin/activate

# install deps
pip install pygame RPi.GPIO
