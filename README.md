# Предисловие

Туториал поможет развернуть чат-бота Telegram, использующего API OpenAI, как локально, так и в Docker контейнере на облачном сервере. 

Библиотеки:
  - [openai](https://pypi.org/project/openai/)
  - [python-telegram-bot](https://pypi.org/project/python-telegram-bot/)

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

1. В `Makefile` введите токены Telegram и OpenAI:
   ```
   TELEGRAM_BOT_TOKEN=1235
   OPENAI_API_KEY=1234
   ```
   
2. Установка зависимостей, генерация файла `.env`:
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

# Часть 2: Деплой Docker контейнера

Для деплоя контейнера на облачный сервер потребуется:
- Скаченная программа [Docker](https://www.docker.com/products/docker-desktop/)
- Аккаунт в [DockerHub](https://hub.docker.com/)
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
   > Для публикации образа в [DockerHub](https://hub.docker.com/) нужно залогиниться через CLI командой `docker login`

1. Собираем образ под Linux Debian:
   ```
   make build
   ```

6. Публикуем образ в DockerHub:
   ```
   make push
   ```
   
---

## Облачный сервер

1. Подойдет почти любой облачный сервис, например https://timeweb.cloud/
2. Для доступа к API OpenAI разворачиваем сервер в Нидерландах
3. Выбираем Debian 12 
4. Когда сервер загрузится и сгенерируется root-пароль, подключаемся к серверу по SSH

---

## Установка Docker

1. Обновляем систему и настраиваем репозиторий для Docker:
   ```
   sudo apt-get update
   sudo apt-get install ca-certificates curl
   sudo install -m 0755 -d /etc/apt/keyrings
   sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
   sudo chmod a+r /etc/apt/keyrings/docker.asc
   echo \
     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
     sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   sudo apt-get update  
   ```

2. [Установика Docker](https://docs.docker.com/engine/install/debian/):
   ```
   sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
   ```

3. Тестируем установку:
   ```
   sudo docker run hello-world
   ```

## Скачивание и запуск образа

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
   
