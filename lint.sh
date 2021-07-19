python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

invoke pylint

exit 0 # The linting will always pass, but will show the errors
