import beep
import os
import random
import datetime
import time
from excel_operations import ExcelOperations
from udp.udp_receive import UDPReceive
from dotenv import load_dotenv

load_dotenv()

class Unspoken:
    def __init__(self,reaction_time_sheet_path):
        self.excel_operations=ExcelOperations(reaction_time_sheet_path)
        self.udp_receive = UDPReceive(os.environ['MATSUKI7_IP'], 12345)

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
        while True:
            try:
                # 30秒から60秒の間で乱数を生成
                random_time=random.randint(30,60)
                # random_timeの秒数分待機
                time.sleep(random_time)
                
                self.rac_time_measure()
                self.excel_operations.rac_time_excel(self.start_time,self.end_time)
            except Exception as e:
                print(e)
                exit(1)
