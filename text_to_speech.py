from gtts import gTTS
from playsound import playsound
import time
import os
file_name = 'sample.mp3'

# 영어 문장
# text = 'Can I help you?'
# file_name = 'sample.mp3'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)

# from playsound import playsound
# playsound(file_name) #.mp3 파일 재생

# 한글 문장
# text = '파이썬을 배우면 이런 것도 할 수 있어요'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)

# playsound(file_name)

def play(text):
    tts_ko = gTTS(text=text, lang='ko')
    tts_ko.save(file_name)
    playsound(file_name)
    os.remove(file_name)

time.sleep(2)

text = '응급 상황이 파악되었습니다. 신속히 도와드릴 수 있게 해드릴게요.'
play(text)