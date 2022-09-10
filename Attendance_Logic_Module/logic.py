
from clean_data import clean_class
import pandas as pd


for x in range(1, 5):
  globals()['data%s' % x] = pd.read_csv('test' + str(x) + '.csv', encoding ="latin1")
# Concatanete them
df = pd.concat([data1, data2 ,data3, data4])
df = df.sort_values(['employee_name' , 'timestamp', 'camera_id'])
df['unified_id'] = df['camera_id']
cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df = df[cols]

df['unified_id'] = df['unified_id'].replace(2, 1)
df['unified_id'] = df['unified_id'].replace(4, 3)
####df['unified_id'] = df['unified_id'].replace(6, 5)