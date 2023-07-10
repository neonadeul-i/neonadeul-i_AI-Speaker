from email.mime import audio
import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound

def speak(text ,lang="ko", speed=False):
    tts = gTTS(text=text, lang=lang , slow=speed)
    tts.save("tts.mp3")
    playsound("tts.mp3")

r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print('듣는중')
        audio = r.listen(source)
        
    try:
        data = r.recognize_google(audio, language='ko')
    except:
        speak('제가 잘 이해하지 못했어요.')
    print(data)
    if "나리야" in data or "날이야" in data:
        speak("넹")
        print("에리스 : 넹")
    else:
        speak("다시 불러주세요")