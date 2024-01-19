import openpyxl

class ExcelOperations:
    def __init__(self, reaction_time_sheet_path):
        self.reaction_time_sheet_path = reaction_time_sheet_path

    # 反応時間を記録する
    def rac_time_excel(self):
        # excelシートを読み込む
        wb = openpyxl.load_workbook(self.reaction_time_sheet_path)
        sheet = wb.active
        # 最終行を取得
        last_row = sheet.max_row
        # 回数カラムに書き込む
        sheet.cell(row=last_row + 1, column=1, value=last_row)
        # reaction_timeカラムに書き込む
        sheet.cell(row=last_row + 1, column=2, value=(self.end_time-self.start_time).total_seconds())
        # measurement_timeにself.conv_start_timeとself.end_timeの差分を%M:%s形式で書き込む
        # sheet.cell(row=last_row + 1, column=3, value=(self.conv_start_time-self.end_time))

        # 保存
        wb.save(self.reaction_time_sheet_path)