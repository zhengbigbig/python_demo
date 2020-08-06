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
# 修改
df.loc[df['sex'] == 0, 'sex'] = '女性'
df.loc[df['sex'] == 1, 'sex'] = '男性'
print(df)
'''
   name sex
0   jzz  女性
1   zbb  男性
2  jzzh  男性
'''
df.rename(columns={'name': '用户名', 'sex': '性别'}, inplace=True)
print(df)
'''
    用户名  性别
0   jzz  女性
1   zbb  男性
2  jzzh  男性
'''
df.rename(index={1: 111, 2: 222}, inplace=True)
print(df)
'''
      用户名  性别
0     jzz  女性
111   zbb  男性
222  jzzh  男性
'''
print(df.iloc[:5])  # 和行标签无关，是按位置来取
'''
      用户名  性别
0     jzz  女性
111   zbb  男性
222  jzzh  男性
'''
# 重置索引 drop 是否清理掉之前索引，inplace是否作用数据
df.reset_index(drop=True, inplace=True)
print(df)
'''
    用户名  性别
0   jzz  女性
1   zbb  男性
2  jzzh  男性
'''
# 查询
print(df[df['性别'] == '女性'])
'''
   用户名  性别
0  jzz  女性
'''
print(df[~(df['性别'] == '女性')])
'''
    用户名  性别
1   zbb  男性
2  jzzh  男性
'''
print(df[(df['性别'] == '男性') & (df['用户名'] == 'zbb')])
'''
   用户名  性别
1  zbb  男性
'''
# between inclusive 是否包含左右
df['level'] = np.where(df['性别'] == '男性', 1, 0)
print(df[df['level'].between(0, 1, inclusive=True)])
'''
    用户名  性别  level
0   jzz  女性      0
1   zbb  男性      1
2  jzzh  男性      1
'''
# isin
print(df[df['level'].isin([0])])
'''
   用户名  性别  level
0  jzz  女性      0
'''
