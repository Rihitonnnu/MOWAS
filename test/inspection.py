import pandas as pd

# ファイルパス
file_path = "../data/reaction_time/20240127/kumamoto/160855.xlsx"

# Excelファイルを読み込む
df = pd.read_excel(file_path)

# reaction_timeの列を取り出す
reaction_time_a = df["reaction_time_a"]
reaction_time_b = df["reaction_time_b"]

# reaction_time_a,reaction_time_bをlistに変換する
reaction_time_a = reaction_time_a.dropna().values.tolist()
reaction_time_b = reaction_time_b.dropna().values.tolist()

# mean_aとmean_bのt検定を行う
from scipy import stats
t_statistic, p_value=stats.ttest_ind(reaction_time_a, reaction_time_b)

# 結果を表示する
print("T-statistic:", t_statistic)
print("P-value:", p_value)
# print(mean_a)
# print(mean_b)
# print(result)
