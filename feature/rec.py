import speech_recognition as sr
import beep

listener = sr.Recognizer()

def run():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            voice_text = listener.recognize_google(voice,language="ja-JP")
            beep.low()
            print(voice_text)
    except:
        print('聞き取れませんでした')
