from telegram.ext import MessageHandler, filters
from config.telegram_bot import application
from handlers.message_handlers import chatgpt_reply
from handlers.audio_handlers import audio_reply
from handlers.image_handlers import image_reply
from handlers.video_handlers import video_reply


# Регистрация обработчика текстовых сообщений
message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, chatgpt_reply)
application.add_handler(message_handler)

# Регистрация обработчика аудио сообщений
audio_handler = MessageHandler(filters.VOICE, audio_reply)
application.add_handler(audio_handler)

# Регистрация обработчика изображений
photo_handler = MessageHandler(filters.PHOTO, image_reply)
application.add_handler(photo_handler)

# Регистрация обработчика видео
video_handler = MessageHandler(filters.VIDEO, video_reply)
application.add_handler(video_handler)

# Запуск бота
application.run_polling()
