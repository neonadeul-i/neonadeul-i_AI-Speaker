import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('듣는중')
    audio = r.listen(source)  # 마이크로부터 음성 확인
    
try:
    text = r.recognize_google(audio, language='en-US')
    with open('sample.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print(text)
    
except sr.UnknownValueError:
    print('인식 실패') 
except sr.RequestError as e:
    print('요첯 실패: {e}'.format(e))  # API Key, 네트워크 단절 등등의 오류