# данные пользователя на Docker Hub
USERNAME=UserNameDockerHub
REPO=RepositoryNameDockerHub
TAG=v1
TELEGRAM_BOT_TOKEN=1235
OPENAI_API_KEY=1234

IMAGE = $(USERNAME)/$(REPO):$(TAG)

PYTHON=python
ifeq ($(OS),Windows_NT)
    PIP=.venv\Scripts\pip
    PYTHON_VENV=.venv\Scripts\python
    SHELL := cmd.exe
    VENV_CREATE=python -m venv .venv
    ENV_FILE_CREATE=@echo TELEGRAM_BOT_TOKEN=$(TELEGRAM_BOT_TOKEN) > .env & @echo OPENAI_API_KEY=$(OPENAI_API_KEY) >> .env
    CLEAN_VENV=if exist .venv rmdir /s /q .venv
    CLEAN_ENV=if exist .env del .env
    CLEAN_PYCACHE=del /s /q __pycache__ & del /s /q *.pyc
else
    PIP=.venv/bin/pip
    PYTHON_VENV=.venv/bin/python
    VENV_CREATE=python3 -m venv .venv
    ENV_FILE_CREATE=echo "TELEGRAM_BOT_TOKEN=$(TELEGRAM_BOT_TOKEN)" > .env && echo "OPENAI_API_KEY=$(OPENAI_API_KEY)" >> .env
    CLEAN_VENV=rm -rf .venv
    CLEAN_ENV=rm -f .env
    CLEAN_PYCACHE=find . -type f -name '*.pyc' -delete && find . -type d -name '__pycache__' -delete
endif

# создание виртуального окружения
setup:
	@echo "Setup venv, install requirements and create .env"
	$(VENV_CREATE)
	$(PIP) install -r requirements.txt
	make create-env

# создание файла .env
create-env:
	$(ENV_FILE_CREATE)

# запуск приложения
run:
	@echo "Run app"
	$(PYTHON_VENV) app.py

# сборка образа
build:
	@echo "Build image for $(IMAGE)"
	docker build --platform linux/amd64 -t $(IMAGE) .

# публикация образа
push:
	@echo "Push image to $(IMAGE)"
	docker push $(IMAGE)

# очистка окружения
clean:
	@echo "Clean venv and .env"
	$(CLEAN_VENV)
	$(CLEAN_ENV)
	$(CLEAN_PYCACHE)