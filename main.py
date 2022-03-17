from asyncore import poll
from Packages import ocr
from Packages import polly
from Packages import play_sound
from Packages import speach_recognition
import time


if __name__ == '__main__':
    # OCR
    ocr_result = ocr.opencv_image_process('./resources/test/kor_text.png', 'kor')
    print(ocr_result)

    # Polly
    polly.polly(ocr_result)
    play_sound.mp3tomp4()
    duration = play_sound.get_duration('./resources/temp/tts.mp4')
    play_sound.play(duration, './resources/temp/tts.mp4')

    # Seach
    speach_recognition.read_voice('./resources/voice/OKmin.wav')