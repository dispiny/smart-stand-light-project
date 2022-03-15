import os
import sys
import shutil
from boto3 import client

def polly(text):
    polly = client("polly", region_name="ap-northeast-2")
    response = polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId="Seoyeon")

    stream = response.get("AudioStream")

    with open('./resources/temp/tts.mp3', 'wb') as f:
        data = stream.read()
        f.write(data)
        
