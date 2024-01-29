
from conversation import Conversation
from unspoken import Unspoken
import os
# import view.option_window
import udp.udp_receive
import openpyxl
import datetime
import beep

# 現在時刻を取得
now=datetime.datetime.now()
ymd=now.strftime('%Y%m%d')
hms=now.strftime('%H%M%S')

# 名前を入力
name='kawanishi'
mowas_use=False


# ディレクトリやファイル作成
# try:
#     os.makedirs('../sound/{}'.format(now.strftime('%Y%m%d')))
# except FileExistsError:
#     pass
try:
    os.makedirs('../log')
except FileExistsError:
    pass
try:
    os.makedirs('../data/reaction_time/{}/{}'.format(now.strftime('%Y%m%d'),name))
    os.makedirs('../data/reaction_time/{}/{}/unspoken/'.format(now.strftime('%Y%m%d'),name))
except FileExistsError:
    pass

#excelファイル作成
wb = openpyxl.Workbook()
sheet = wb.active
# 回数カラムをexcelで作成
sheet['A1'] = 'cnt'
# reaction_timeカラムをexcelで作成
sheet['B1'] = 'reaction_time'
sheet['C1'] = 'measurement_time'
sheet['D1'] = 'guide_acc_time'

# 眠くなりかけるまで待機
# while True:
#     try:
#         is_sleepy=udp.udp_receive.UDPReceive(os.environ['MATSUKI7_IP'],12345).is_sleepy()
#         print(is_sleepy)
#         if is_sleepy:
#             # beep音を鳴らす
#             beep.high()
#             break
#     except Exception as e:
#         pass

# MOWAS使用
if mowas_use:
    reaction_time_sheet_path='../data/reaction_time/{}/{}/{}.xlsx'.format(ymd,name,hms)
    wb.save(reaction_time_sheet_path)
    Conversation(reaction_time_sheet_path).run()

# MOWAS使用しない
if mowas_use is False:
    reaction_time_sheet_path='../data/reaction_time/{}/{}/unspoken/{}.xlsx'.format(ymd,name,hms)
    wb.save(reaction_time_sheet_path)
    Unspoken(reaction_time_sheet_path).run()
