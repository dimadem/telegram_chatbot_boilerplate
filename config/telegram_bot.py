from telegram.ext import Application 
from .tokens import TELEGRAM_BOT_TOKEN 

# Создание экземпляра бота
application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()