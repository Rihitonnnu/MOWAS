import speech_recognition as sr
import beep
from SyntheticVoice import SyntheticVoice

class Rec:
    def __init__(self):
        self.listener = sr.Recognizer()
        self.rec_cnt=0

    def run(self):
        try:
            with sr.Microphone() as source:
                # beep.high()
                voice = self.listener.listen(source)
                human_input = self.listener.recognize_google(voice,language="ja-JP")
                beep.low()
                print(human_input)
                return human_input
        except:
            print('聞き取れませんでした')
            if self.rec_cnt<1:
                SyntheticVoice().speaking('すみません、聞き取れませんでした。ビープ音の後にもう一度お願いします。')
                self.rec_cnt+=1
                beep.high()
                self.run()

            return None

# Rec().run()
