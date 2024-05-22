from telegram.ext import MessageHandler, CommandHandler, filters
from config.telegram_bot import application 
from handlers.message_handlers import chatgpt_reply 
from handlers.command_handlers import start_reply

# Регистрация обработчика текстовых сообщений
message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, chatgpt_reply)
application.add_handler(message_handler)

# Регистрация обработчика команд
start_command_handler = CommandHandler("start", start_reply)
application.add_handler(start_command_handler)

# Запуск бота
application.run_polling()