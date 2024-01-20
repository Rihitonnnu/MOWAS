import pandas as pd

# 眠いかどうかを聞くかどうか判別する
class QuestionJudge:
    def __init__(self,reaction_time_sheet_path):
        self.reaction_time_sheet_path = reaction_time_sheet_path

        # excelファイルを読み込む
        self.df = pd.read_excel(self.reaction_time_sheet_path, sheet_name='Sheet')
        self.threshold_judge_cnt=0
    
    # しきい値
    def threshold_judge(self):
        # excelファイルの最終行のreaction_timeを取得
        reaction_time = self.df['reaction_time'].iloc[-1]
        if reaction_time>1.5:
            self.threshold_judge_cnt+=1
    
    # 眠くなっている可能性がある場合はTrueを返す
    def run(self):
        # reaction_timeの平均値を取得
        # print(self.df['reaction_time'].mean())
        self.threshold_judge()

        # 累計3回以上しきい値を超えていたら眠くなっている可能性があると判断
        if self.threshold_judge_cnt>=3:
            self.threshold_judge_cnt=0
            return True
        
        return False

# result=QuestionJudge('../data/reaction_time/20240119/kawanishi/165732.xlsx').run()
# print(result)
