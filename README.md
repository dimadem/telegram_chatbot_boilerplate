# Команды

# установка проекта

- устанавливаем зависимости и создаем .env файл

```
make setup
```

- Вставляем токены бота Telegram & API key OpenAi в .env

- Запускаем проект

```
make run
```

- удаляем .venv / .env / cache/ etc.

```
make clean
```

---

# Структура проекта

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
├── requirements.txt
└── README.md
```

- `config/` - конфигурационные файлы

  - `openai_client.py` - настройки доступа к сервису OpenAI
  - `telegram_bot.py` - настройки создания экземпляра бота Telegram
  - `tokens.py` - токены

- `handlers/` - обработчики сообщений и команд

  - `command_handlers.py` - модуль с обработчиками команд (`/start`, `/help`, `/clear`, ...)
  - `message_handlers.py` - модуль с обработчиками текстовых сообщений

- `utils/` - вспомогательные функции

- `app.py` - главный файл приложения

- `requirements.txt` - зависимости проекта

# разворачивание в сети

## сервер на Debian

- Можно воспользоваться любым облачным сервисом, в этом примере мы воспользуемся https://timeweb.cloud/
- Для доступа к API OpenAI, разворачиваем облачный сервер в Нидерландах.

- Выбираем Debian 12

- Когда сервер загрузился и сгенерировался root-пароль, можно подключаться к серверу

- Используем ssh подключение и root пароль для доступа к cli сервера

---

## [установка Docker](https://docs.docker.com/engine/install/debian/)

- обновление системы и настройка apt репозитория Docker

```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

- установка Docker

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

- тест

```
sudo docker run hello-world
```

---
