import speech_recognition as sr
import sounddevice as sd

# wf = wave.open("../sound/test.wav", "rb")
# filename = glob.glob('test.wav')
# print(filename)
# exit(1)


def speech_recognition(filename):
    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio = r.record(source)
    speechText = r.recognize_google(audio, language='ja-JP')
    print(speechText)
    return speechText


speech_recognition()
