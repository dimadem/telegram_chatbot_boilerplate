FROM python:3.9

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0


WORKDIR /app

# копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY config/ ./config/
COPY handlers/ ./handlers/
COPY utils/ ./utils/
COPY app.py .

# команда запуска приложения
CMD ["python", "app.py"]