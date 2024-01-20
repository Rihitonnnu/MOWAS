import speech_recognition as sr
import beep
from SyntheticVoice import SyntheticVoice

listener=sr.Recognizer()

class Rec:
    def __init__(self):
        self.rec_cnt=0

    def run(self):
        for _ in range(2):
            try:
                with sr.Microphone() as source:
                    # beep.high()
                    voice = listener.listen(source)
                    human_input = listener.recognize_google(voice,language="ja-JP")
                    beep.low()
                    print(human_input)
                    return human_input
            except:
                print('聞き取れませんでした')
                self.rec_cnt+=1

                if self.rec_cnt<2:
                    # SyntheticVoice().speaking('すみません、聞き取れませんでした。ビープ音の後にもう一度お願いします。')
                    self.rec_cnt+=1
                    beep.high()
                else:
                    return None
            
            else:
                break

# Rec().run()
