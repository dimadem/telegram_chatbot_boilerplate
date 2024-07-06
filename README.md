# Choose language / Выберите язык

- [English](#preface)
- [Русский](#предисловие)

# Preface

This tutorial will help you deploy a Telegram chatbot using the OpenAI API, both locally and in a Docker container on a cloud server.

Libraries:

- [openai](https://pypi.org/project/openai/)
- [python-telegram-bot](https://pypi.org/project/python-telegram-bot/)
- [Jupyter Notebook](https://pypi.org/project/notebook/)

## Project Structure

```
telegram_chatbot_boilerplate/
│
├── config/
│   ├─── openai_client.py
│   ├─── telegram_bot.py
│   └─── tokens.py
│
├── handlers/
│   ├── __init__.py
│   ├── command_handlers.py
│   └── message_handlers.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── app.py
├── Dockerfile
├── Makefile
└── requirements.txt
```

- `config/` - configuration files
- `handlers/` - message and command handlers
- `utils/` - helper functions
- `app.py` - main application file
- `Dockerfile` - script for creating Docker image
- `Makefile` - build process automation
- `requirements.txt` - project dependencies

---
# Part 0: Creating a Repository

- Click the **USE THIS TEMPLATE** button in the top right
- Name your project
- The content in the repository will be used for the hackathon

---
  
# Part 1: Local Installation

For local project installation, you will need:

- VPN server connection for access to OpenAI API
- Telegram bot token
- OpenAI API token
- Linux or MacOS operating system

## Telegram Bot Token

First, you need to obtain a token for access to your bot's HTTP API:

1. Find the `@BotFather` bot in Telegram
2. Send him the `/newbot` command
3. Enter the project name and bot name
4. Copy the received token

## Project Installation
1. Clone the repository
   ```
   git clone github.com/yourreponame
   ```
2. Enter the Telegram and OpenAI tokens in the `Makefile`:
   ```
   TELEGRAM_BOT_TOKEN=1235
   OPENAI_API_KEY=1234
   ```
3. Install dependencies, generate `.env` file:
   ```
   make setup
   ```

## Running the Project
1. Launch the bot locally
```
make run
```
2. Open the Telegram bot and send a message
> Messages in the Telegram bot and in the terminal are duplicated.
3. To remove .venv, .env, cache, and other temporary files:
```
make clean
```

---

# Part 2: Development on a Cloud Server

For remote development, you will need:

- Server Access (ssh user@ip & password)
- Jupyter Notebook
- Visual Studio Code

#### Pre-installed software on the server:
- vim
- build-essential
- python3
- python3-venv
- docker-ce
- docker-ce-cli
- docker-buildx-plugin
- docker-compose-plugin

# Remote Development
0. Log into the server
```
ssh -i PATH_TO_YOUR_KEY.pem admin@SERVER_IP_ADDRESS
```
1. Clone your repository (via https) into a separate folder on the server
```
git clone <repositorylink>
```
2. Enter the Telegram and OpenAI tokens in the `Makefile`:
```
TELEGRAM_BOT_TOKEN=1235
OPENAI_API_KEY=1234
```
3. Install dependencies, generate `.env` file:
```
make setup
```
4. Launch Jupyter Notebook
```
make notebook
```
5. Copy after **token=** to your notes:
```
http://127.0.0.1:8888/tree?token=YOUR_PERSONAL_TOKEN
```
6. On your **personal device**, create a tunnel:
```
ssh -NL 8888:localhost:8888 root@SERVER_IP_ADDRESS
```
or (depending on how you're logged into the server)
```
ssh -NL 8888:localhost:8888 admin@SERVER_IP_ADDRESS
```
> Also, if you're logged into the server using a key (-i PATH_TO_YOUR_KEY.pem), you need to specify it when creating the tunnel
7. Open in browser:
```
http://localhost:8888
```
8. Paste the token you copied in step **5** into the "Password or token" field and click Login.
9. Use it

---

# Running Docker Container

To deploy a container to a cloud server, you will need:

- Downloaded [Docker](https://www.docker.com/products/docker-desktop/) program
- Account on [DockerHub](https://hub.docker.com/)
- [Create a repository](https://docs.docker.com/docker-hub/repos/create/)
- Telegram bot token
- OpenAI API token
- Linux or MacOS operating system

1. In the `Makefile`, add **username** and **repositoryname** to the existing tokens:
```
USERNAME=UserNameDockerHub
REPO=RepositoryNameDockerHub
TAG=v1
TELEGRAM_BOT_TOKEN=1235
OPENAI_API_KEY=1234
```
2. Build the image for Linux Debian:
```
make build
```
3. Run the container with the application
```
make dockerrun
```
4. Also, you can publish the image on DockerHub:
```
make push
```

---

## Downloading and Running the Published Image

1. Find the published image on DockerHub:
```
docker search username/projectname
```
2. Download the image:
```
docker pull username/projectname:v1
```
3. Run the container with Telegram bot and OpenAI API tokens:
```
sudo docker run -i -t -e TELEGRAM_BOT_TOKEN=YOURTOKEN -e OPENAI_API_KEY=YOURTOKEN username/projectname:v1
```
4. Open the Telegram bot and send a message
> Messages in the Telegram bot and in the terminal are duplicated.

--- --- --- 
--- --- ---

# Предисловие

Туториал поможет развернуть чат-бота Telegram, использующего API OpenAI, как локально, так и в Docker контейнере на облачном сервере.

Библиотеки:

- [openai](https://pypi.org/project/openai/)
- [python-telegram-bot](https://pypi.org/project/python-telegram-bot/)
- [Jupyter Notebook](https://pypi.org/project/notebook/)

## Структура проекта

```
telegram_chatbot_boilerplate/
│
├── config/
│   ├─── openai_client.py
│   ├─── telegram_bot.py
│   └─── tokens.py
│
├── handlers/
│   ├── __init__.py
│   ├── command_handlers.py
│   └── message_handlers.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── app.py
├── Dockerfile
├── Makefile
└── requirements.txt
```

- `config/` - конфигурационные файлы
- `handlers/` - обработчики сообщений и команд
- `utils/` - вспомогательные функции
- `app.py` - главный файл приложения
- `Dockerfile` - скрипт для создания Docker образа
- `Makefile` - автоматизация процесса сборки
- `requirements.txt` - зависимости проекта

---
# Часть 0: Создание репозитория

- нажми кнопку справа сверху **USE THIS TEMPLATE**
- назови проект
- контент в репозитории будет использоваться для хакатона

---
  
# Часть 1: Локальная установка

Для локальной установки проекта потребуется:

- подключение к VPN серверу для доступа к API OpenAI
- токен Telegram бота
- токен API OpenAI
- операционная система Linux или MacOS

## Токен Телеграм бота

Для начала нужно получить токен для доступа к HTTP API вашего бота:

1. Найдите в Telegram бота `@BotFather`
2. Отправьте ему команду `/newbot`
3. Введите имя проекта и имя бота
4. Скопируйте полученный токен

## Установка проекта
0. Склонировать репозиторий
   ```
   git clone github.com/yourreponame
   ```
2. В `Makefile` введите токены Telegram и OpenAI:
   ```
   TELEGRAM_BOT_TOKEN=1235
   OPENAI_API_KEY=1234
   ```
3. Установка зависимостей, генерация файла `.env`:
   ```
   make setup
   ```

## Запуск проекта

1. Запускаем бота локально
   ```
   make run
   ```
2. Открываем Telegram бота и отправляем сообщение

   > Сообщения в Telegram боте и в терминале дублируются.

3. Для удаления .venv, .env, cache и других временных файлов:
   ```
   make clean
   ```

---

# Часть 2: Разработка на облачном сервере

Для удаленной разработки потребуется:

- Доступ к Серверу (ssh user@ip & password)
- Jupyter Notebook
- Visual Studio Code

#### Предустановленный софт на сервере:
- vim
- build-essential
- python3
- python3-venv
- docker-ce
- docker-ce-cli
- docker-buildx-plugin
- docker-compose-plugin

# Удаленная разработка
0. Заходим на сервер
  ```
  ssh -i PATH_TO_YOUR_KEY.pem admin@SERVER_IP_ADDRESS
  ```

1. Клонируем (по https) свой репозиторий в отдельную папку на сервер
   ```
   git clone <repositorylink>
   ```

3. В `Makefile` введите токены Telegram и OpenAI:
   ```
   TELEGRAM_BOT_TOKEN=1235
   OPENAI_API_KEY=1234
   ```
4. Установка зависимостей, генерация файла `.env`:
   ```
   make setup
   ```
5. Запускаем Jupyter Notebook
   ```
   make notebook
   ```
6. Копируем после **token=** в заметки:
   ```
   http://127.0.0.1:8888/tree?token=YOUR_PERSONAL_TOKEN
   ```
7. На своем **персональном устройстве** создаем туннель:
   ```
   ssh -NL 8888:localhost:8888 root@SERVER_IP_ADDRESS
   ```

   или (в зависимости от того, как вы залогинены на сервере)

   ```
   ssh -NL 8888:localhost:8888 admin@SERVER_IP_ADDRESS
   ```
  также если вы залогинены на сервере с использованием ключа (-i PATH_TO_YOUR_KEY.pem), его нужно указать при создании тунеля
   
9. Открываем в браузере;
   ```
   http://localhost:8888
   ```
10. Вставляем токен, который скопировали на шаге **5**, в поле "Password or token" и нажимаем Login.
11. Пользуемся

---

# Запуск Docker контейнера

Для деплоя контейнера на облачный сервер потребуется:

- Скаченная программа [Docker](https://www.docker.com/products/docker-desktop/)
- Аккаунт в [DockerHub](https://hub.docker.com/)
- [Создать репозиторий](https://docs.docker.com/docker-hub/repos/create/)
- токен Telegram бота
- токен API OpenAI
- операционная система Linux или MacOS

1. В `Makefile` добавим к уже имеющимся токенам, **username** и **repositoryname**:

   ```
   # данные пользователя на Docker Hub
   USERNAME=UserNameDockerHub
   REPO=RepositoryNameDockerHub
   TAG=v1
   TELEGRAM_BOT_TOKEN=1235
   OPENAI_API_KEY=1234
   ```
#### Для публикации образа в [DockerHub](https://hub.docker.com/) нужно залогиниться через CLI командой `docker login`


2. Собираем образ под Linux Debian:

   ```
   make build
   ```

3. Запускаем контейнер с приложением

  ```
   make dockerrun
  ```

4. Также, можно опубликовать образ в DockerHub:

   ```
   make push
   ```

---

## Скачивание и запуск опубоикованного образа

1. Находим опубликованный образ в DockerHub:

   ```
   docker search username/projectname
   ```

2. Скачиваем образ:

   ```
   docker pull username/projectname:v1
   ```

3. Запускаем контейнер с токенами Telegram бота и OpenAI API:

   ```
   sudo docker run -i -t -e TELEGRAM_BOT_TOKEN=YOURTOKEN -e OPENAI_API_KEY=YOURTOKEN username/projectname:v1
   ```

4. Открываем Telegram бота и отправляем сообщение
   > Сообщения в Telegram боте и в терминале дублируются.
