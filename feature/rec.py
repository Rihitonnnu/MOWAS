import speech_recognition as sr
import beep

listener = sr.Recognizer()

def run():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            human_input = listener.recognize_google(voice,language="ja-JP")
            beep.low()
            print(human_input)
            return human_input
    except:
        print('聞き取れませんでした')
        return None

