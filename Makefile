# данные пользователя на Docker Hub
USERNAME=UserNameDockerHub
REPO=RepositoryNameDockerHub
TAG=v1
TELEGRAM_BOT_TOKEN=1235
OPENAI_API_KEY=1234

IMAGE = $(USERNAME)/$(REPO):$(TAG)


PYTHON=python3
PIP=.venv/bin/pip
PYTHON_VENV=.venv/bin/python

# создание виртуального окружения
setup:
	@echo "Setup venv, install requirements and create .env"
	$(PYTHON) -m venv .venv
	$(PIP) install -r requirements.txt
	make create-env

# создание файла .env
create-env:
	echo "TELEGRAM_BOT_TOKEN=$(TELEGRAM_BOT_TOKEN)" > .env
	echo "OPENAI_API_KEY=$(OPENAI_API_KEY)" >> .env

# запуск приложения
run:
	@echo "Run app"
	$(PYTHON_VENV) app.py

# запуск приложения в Docker
dockerrun:
	@echo "Docker run"
	sudo docker run -i -t -e TELEGRAM_BOT_TOKEN=$(TELEGRAM_BOT_TOKEN) -e OPENAI_API_KEY=$(OPENAI_API_KEY) $(IMAGE)

# сборка образа
build:
	@echo "Build image for $(IMAGE)"
	sudo docker build --platform linux/amd64 -t $(IMAGE) .

# запуск Jupiter Notebook
notebook:
	@echo "Run Jupiter Notebook"
	@. .venv/bin/activate && $(PYTHON_VENV) -m jupyter notebook --no-browser --port=8888 --ip=0.0.0.0 --allow-root

# публикация образа
push:
	@echo "Push image to $(IMAGE)"
	sudo docker push $(IMAGE)

# очистка окружения
clean:
	@echo "Clean venv and .env"
	rm -rf .venv
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -f .env

.PHONY: setup create-env run dockerrun build push clean
