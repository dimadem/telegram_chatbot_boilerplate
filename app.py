from telegram.ext import MessageHandler, filters
from config.telegram_bot import application 
from handlers.message_handlers import chatgpt_reply 


# Регистрация обработчика текстовых сообщений
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chatgpt_reply))

# Запуск бота
application.run_polling()
