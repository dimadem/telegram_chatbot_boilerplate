# данные пользователя на Docker Hub
USERNAME=UserNameDockerHub
REPO=RepositoryNameDockerHub
TAG=v1

IMAGE = $(USERNAME)/$(REPO):$(TAG)


PYTHON=python3
PIP=.venv/bin/pip
PYTHON_VENV=.venv/bin/python

# создание виртуального окружения
setup:
	$(PYTHON) -m venv .venv
	$(PIP) install -r requirements.txt
	make create-env

# создание файла .env
create-env:
	echo "TELEGRAM_BOT_TOKEN=" > .env
	echo "OPENAI_API_KEY=" >> .env

# запуск приложения
run:
	$(PYTHON_VENV) app.py

# сборка образа
build:
	docker build --platform linux/amd64 -t $(IMAGE) .

# публикация образа
push:
	docker push $(IMAGE)

# очистка окружения
clean:
	rm -rf .venv
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -f .env