import numpy as np
import pandas as pd
import os

os.chdir('/Users/zhengzhiheng/PycharmProjects/untitled3')
df = pd.read_csv('test.csv', dtype=str, encoding='utf-8')
print(df.head(5))
'''
   name sex    asset
0   jzz   0  $19,300
1   zbb   1  $17,200
2  jzzh   1   $1,000
'''
print(df.info())
df['new_asset'] = df['asset'].str.strip('$')
df['new_asset'] = df['new_asset'].str.replace(',', '')
df['new_asset'] = df['new_asset'].astype(int)
print(df)
'''
   name sex    asset  new_asset
0   jzz   0  $19,300      19300
1   zbb   1  $17,200      17200
2  jzzh   1   $1,000       1000
'''
print(df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 4 columns):
 #   Column     Non-Null Count  Dtype 
---  ------     --------------  ----- 
 0   name       3 non-null      object
 1   sex        3 non-null      object
 2   asset      3 non-null      object
 3   new_asset  3 non-null      int64 
dtypes: int64(1), object(3)
memory usage: 224.0+ bytes
'''
