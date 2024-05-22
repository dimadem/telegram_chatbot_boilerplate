import base64
import cv2
import subprocess

def frames_to_base64(video_file):
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

async def image_to_base64(image_file):
    image_bytes = await image_file.download_as_bytearray()
    return base64.b64encode(image_bytes).decode('utf-8')

def convert_to_ogg(file_path):
    ogg_file = file_path.replace(".mov", ".ogg")
    subprocess.run(["ffmpeg", "-i", file_path, ogg_file])
    return ogg_file