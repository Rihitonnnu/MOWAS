from SyntheticVoice import SyntheticVoice
from udp.udp_receive import UDPReceive
from rec import Rec
import os
import time
import beep
import datetime
from dotenv import load_dotenv
load_dotenv()


class Demo:
    def __init__(self):
        self.synthetic_voice = SyntheticVoice()
        self.udp_receive = UDPReceive(os.environ['MATSUKI7_IP'], 12345)
        self.rec = Rec()

    # 反応時間計測
    def rac_time_measure(self):
        # 開始時間の取得及び変換
        beep.high()
        self.start_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')
        self.start_time = datetime.datetime.strptime(self.start_time, '%Y/%m/%d %H:%M:%S.%f')

        while True:
            date=None
            date=self.udp_receive.get_end_time()
            if date is not None:
                # dateを日付型に変換
                self.end_time=datetime.datetime.strptime(date, '%Y/%m/%d %H:%M:%S.%f')
                break

    def run(self):
        self.synthetic_voice.speaking('デモを始めます')
        # 反応時間計測
        self.rac_time_measure()

        for _ in range(2):
            self.human_input = self.rec.run()
            if isinstance(self.human_input,str):
                break
        
Demo().run()
