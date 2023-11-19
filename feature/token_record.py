import openpyxl
import os
import datetime

if os.path.exists('../data/token.xlsx'):
    write_wb = openpyxl.load_workbook('../data/token.xlsx')
if not os.path.exists('../data/token.xlsx'):
    write_wb = openpyxl.Workbook()
    write_wb.save('../data/token.xlsx')

# シートを会話したときの日時で作成
write_wb.create_sheet(title=datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
write_wb.save("../data/token.xlsx")


def token_record(cb):
    data = [cb.prompt_tokens, cb.completion_tokens, cb.total_tokens]

    # シートを変数に名前で格納
    write_ws = write_wb["Sheet"]
    # cはセル番地でA1のセルを取得する
    c = write_ws["A1"]
    # c2は行列番号でA2のセルを取得する
    c2 = write_ws.cell(1, 2)
    # 変数cにvalueを付けて値を設定する
    c.value = "A1です"
    c2.value = "B1です"

    # Book_write.xlsxに上書保存
    write_wb.save("../data/token.xlsx")
