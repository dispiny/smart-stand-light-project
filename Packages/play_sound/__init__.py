import vlc
import time
from moviepy.editor import *

def get_duration(filename):
    clip = VideoFileClip(filename)
    return clip.duration

def mp3tomp4():
    audio = AudioFileClip("./resources/temp/tts.mp3")

    video = ImageClip('./resources/images/cover.png',duration=audio.duration)
    video = video.set_audio(audio)
    video.write_videofile("./resources/temp/tts.mp4",fps=24, codec="mpeg4")

def play(duration, location):
    media_player = vlc.MediaPlayer()
    media_file = location

    media = vlc.Media(media_file)
    media_player.set_media(media)
    media_player.video_set_scale(0.6)
    time.sleep(1)
    media_player.audio_set_volume(80)
    time.sleep(1)
    media_player.play()
    time.sleep(duration)