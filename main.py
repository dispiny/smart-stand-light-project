from asyncore import poll
from Packages import ocr
from Packages import polly
from Packages import play_sound
import time


if __name__ == '__main__':
    ocr_result = ocr.opencv_image_process('./resources/test/book2.jpg', 'kor')
    print(ocr_result)
    # Polly API Request
    polly.polly(ocr_result)
    play_sound.mp3tomp4()
    duration = play_sound.get_duration('./resources/temp/tts.mp4')
    play_sound.play(duration, './resources/temp/tts.mp4')