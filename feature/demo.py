from SyntheticVoice import SyntheticVoice
from udp.udp_receive import UDPReceive
from rec import Rec
import os
import time
import beep
from dotenv import load_dotenv
load_dotenv()


class Demo:
    def __init__(self):
        self.synthetic_voice = SyntheticVoice()
        self.udp_receive = UDPReceive(os.environ['MATSUKI7_IP'], 12345)
        self.rec = Rec()

    def run(self):
        self.synthetic_voice.speaking('こんにちは。デモを始めます')
        time.sleep(0.5)
        beep.high()
        # 反応時間計測
        self.rac_time_measure()
        for _ in range(2):
            self.human_input = self.rec.run()
            if isinstance(self.human_input,str):
                break

Demo().run()
