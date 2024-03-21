PYTHON=python3
PIP=.venv/bin/pip
PYTHON_VENV=.venv/bin/python

setup:
	$(PYTHON) -m venv .venv
	$(PIP) install -r requirements.txt
	make create-env

create-env:
	echo "TELEGRAM_BOT_TOKEN=" > .env
	echo "OPENAI_API_KEY=" >> .env

run:
	$(PYTHON_VENV) app.py

clean:
	rm -rf .venv
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -f .env