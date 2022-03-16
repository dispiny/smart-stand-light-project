import speech_recognition as sr
# import pyaudio

start_text = [ '오케이 민구', '오케이 밍구', '오켕 민구', '오켕 밍구', '오큉 민구', '오큉 밍구', 'OK 민구', 'OK 밍구', '오퀴이 민구', '오퀴이 밍구']

def read_voice(location):   
    r = sr.Recognizer()

    # mic = Microphone() # 마이크 객체
    
    ## Mic Text (Live)
    # with mic as source:
    #     audio = r.listen(source) # 음성 읽어오기
    #     voice_data = r.recognize_google(audio, language='ko-KR')
    #     return voice_data

    ## File Text
    harvard = sr.AudioFile(location)
    with harvard as source:
        audio = r.record(source)
        output = r.recognize_google(audio, language='ko-KR')

    for i in start_text:
        if output == i:
            print("네?")