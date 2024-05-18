from telegram import Update
from config.openai_client import client
from io import BytesIO
import base64

async def encode_image(image_file):
    image_bytes = await image_file.download_as_bytearray()
    return base64.b64encode(image_bytes).decode('utf-8')

async def image_reply(update, context):
    # Получение объекта File
    image_file = await context.bot.get_file(update.message.photo[-1].file_id)
    print("image_file -> ", image_file)

    # Получение подписи к изображению
    caption = update.message.caption
    print("caption -> ", caption)

    # Кодирование изображения в base64
    base64_image = await encode_image(image_file)
    image_url = image_file.file_path
    print("image_url -> ", image_url)

    # обработка изображения
    description = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": caption,
                    },
                    {
                        "type": "image_url",
                        "image_url":{
                            "url": image_url,
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    # ответ
    reply = description.choices[0].message.content.strip()
    print("assistant:", reply)

    # перенаправление ответа в Telegram
    await update.message.reply_text(reply)