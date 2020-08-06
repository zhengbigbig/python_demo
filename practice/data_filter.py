import pandas as pd
import os
import numpy as np

os.chdir('/Users/zhengzhiheng/PycharmProjects/untitled3')

df = pd.read_csv('test.csv', encoding='utf-8')
print(df)
'''
   name  sex
0   jzz    0
1   zbb    1
2  jzzh    1
'''
# 增
df['level'] = np.where(df['sex'] > 0, 1, 0)
print(df)
'''
   name  sex  level
0   jzz    0      0
1   zbb    1      1
2  jzzh    1      1
'''
# 删
level = df['level']
del df['level']
df.insert(0, 'new_level', level)
print(df)
'''
   new_level  name  sex
0          0   jzz    0
1          1   zbb    1
2          1  jzzh    1
'''
df.drop(labels=['new_level', 'sex'], axis=1, inplace=True)
print(df)
'''
   name
0   jzz
1   zbb
2  jzzh
'''
df.drop(labels=[0, 2], axis=0, inplace=True)
print(df)
'''
   name
1   zbb
'''
