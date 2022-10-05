from gtts import gTTS
from playsound import playsound
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

with open('sample.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    
tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)
playsound(file_name)