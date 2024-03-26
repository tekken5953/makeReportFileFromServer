
import pandas as pd
from datetime import datetime

data1 = {
    'start_date': ['시작일', '20240319'],
    'end_date': ['종료일', '20240324'],
    'account': ['계정', 'airsignal@gmail.net']
}
data2 = {
   'sort': ['날짜', '온도(℃)', '습도(%)']
}
data3 = {
    '날짜': ['2024-03-19', '2024-03-20', '2024-03-21', '2024-03-22', '2024-03-23', '2024-03-24'],
    '온도(℃)': [25, 26, 24, 27, 24, 25],
    '습도(%)': [60, 55, 70, 60, 75, 63]
}


df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

current_date_time = datetime.now()

formatted_date = current_date_time.strftime("%Y%m%d")

file_name = 'C:/Users/sclee/datareport/온도와_습도_보고서_' + formatted_date + '.csv'

with open(file_name, 'w') as f:
    for col_name, col_data in data1.items():
        for item in col_data:
            f.write(f"{item}\t")
        f.write('\n')

    f.write('\n')

    for col_name2, col_data2 in data2.items():
        for item in col_data2:
            f.write(f"{item}\t")
        f.write('\n')

    for idx, row in df3.iterrows():
        for item in row:
            f.write(f"{item}\t")
        f.write('\n')


# merged_df = pd.concat([df1, df2], axis=0)
# merged_df.to_csv(file_name, index=False)

print(f"보고서가 {file_name} 파일로 생성되었습니다.")
