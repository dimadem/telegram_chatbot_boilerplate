from telegram import Update
from config.openai_client import client
from config.openai_client import generate_response
from io import BytesIO

async def audio_reply(update: Update, context):
    if update.message.voice is None:
        return
    # входящее аудио сообщение
    audio_file = await context.bot.get_file(update.message.voice.file_id)
    audio_bytes = BytesIO(await audio_file.download_as_bytearray())
    # запрос транскрипции аудио
    transcription = client.audio.transcriptions.create( model="whisper-1", 
        file=("audio.oga", audio_bytes, "audio/ogg")
    )
    # текст транскрипции
    text = transcription.text.strip()
    # ответ
    reply = generate_response(text)
    # перенаправление ответа в Telegram
    await update.message.reply_text(reply)
    print("user:", audio_file.file_path)
    print("assistant:", reply)