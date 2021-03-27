from youtube_dl import YoutubeDL
from glob import glob
from os.path import isfile, splitext
from os import rename

def get_youtube_audio(url):
    try:
        audio_dl = YoutubeDL({'format':'bestaudio'})
        audio_dl.extract_info(url)
    except Exception:
        return "오디오 처리에 실패하였습니다."
    return None