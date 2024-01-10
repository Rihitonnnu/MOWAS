
from conversation import Conversation
import os
import view.option_window
import udp.udp_receive
import openpyxl
import datetime
import beep

# 現在時刻を取得
now=datetime.datetime.now()
ymd=now.strftime('%Y%m%d')
hms=now.strftime('%H%M%S')

# ディレクトリやファイル作成
try:
    os.mkdir('../sound/{}'.format(now.strftime('%Y%m%d')))
except FileExistsError:
    pass
try:
    os.mkdir('../log')
except FileExistsError:
    pass
try:
    os.mkdir('../data/reaction_time/{}'.format(now.strftime('%Y%m%d')))
except FileExistsError:
    pass

#excelファイル作成
wb = openpyxl.Workbook()
sheet = wb.active
# 回数カラムをexcelで作成
sheet['A1'] = 'num'
# reaction_timeカラムをexcelで作成
sheet['B1'] = 'reaction_time'
reaction_time_sheet_path='../data/reaction_time/{}/{}.xlsx'.format(ymd,hms)
wb.save(reaction_time_sheet_path)

# # 眠くなりかけるまで待機
# while True:
#     is_sleepy=udp.udp_receive.UDPReceive('127.0.0.1',12345).is_sleepy()

#     if is_sleepy:
#         # beep音を鳴らす
#         beep.high()
#         break

Conversation(reaction_time_sheet_path).run()
