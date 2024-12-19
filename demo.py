import pandas as pd

# 外部CSVファイルを読み込む
df = pd.read_csv('./csv/ratio_wave/demo_ratio_wave_data_result.csv')

# 新しいデータフレームを作成
data = []
for i in range(len(df)):
    gets_value = i // 10  # 10行ごとにgetsを増やす
    row = df.iloc[i].copy()
    row['gets'] = gets_value
    data.append(row)

# mac_addressがかぶるようにする（元の行数を維持）
new_df = pd.DataFrame(data)
new_df['mac_address'] = new_df['mac_address'].iloc[:len(new_df)//2].tolist() * 2

# 結果をCSVに出力
new_df.to_csv('output.csv', index=False)

# 結果を表示
print(new_df)
