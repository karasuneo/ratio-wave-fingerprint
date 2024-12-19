import pandas as pd

def aggregate_rssi_by_mac_address(df):
    result = df.groupby('mac_address', as_index=False).agg({
        'gets': 'first',  
        'rssi': 'mean',  
        'type': 'first'   
    })

    result['rssi'] = result['rssi'].round().astype(int)

    return result


# 外部CSVファイルを読み込む
df = pd.read_csv('./csv/ratio_wave/demo_ratio_wave_data_result.csv')

aggregate_rssi_by_mac_address(df).to_csv('output.csv', index=False)

