import base64
import cv2
from telegram import Update
from config.openai_client import client
from io import BytesIO

def frame_to_base64(video_file):
    video = cv2.VideoCapture(video_file.file_path)
    base64Frames = []
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        _, buffer = cv2.imencode(".jpg", frame)
        base64Frames.append(base64.b64encode(buffer).decode("utf-8"))
    video.release()
    cv2.destroyAllWindows()
    return base64Frames

async def video_reply(update, context):
    # получение объекта video_file
    video_file = await context.bot.get_file(update.message.video.file_id)
    print("video_file -> ", video_file)

    audio_bytes = BytesIO(await video_file.download_as_bytearray())
    # запрос транскрипции аудио
    transcription = client.audio.transcriptions.create( model="whisper-1", 
        file=("audio.oga", audio_bytes, "audio/ogg")
    )

    # получение кадров видео
    video_frames = frame_to_base64(video_file)
    print("length of video_frames -> ", len(video_frames))  

    # текст транскрипции
    text = transcription.text.strip()
    print("text -> ", text)

    # подпись к видео
    caption = update.message.caption
    print("caption -> ", caption)

    # обработка видео
    result = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": text,
                    },
                     {
                        "type": "text", 
                        "text": caption,
                    },
                    *map(lambda x: {"image": x, "resize": 768}, video_frames[0::300]),
                ],
            },
        ],
        max_tokens=200,
    )

    # ответ
    reply = result.choices[0].message.content.strip()
    print("assistant:", reply)

    # перенаправление ответа в Telegram
    await update.message.reply_text(reply)