import numpy as np
import pandas as pd
import os

os.chdir('/Users/zhengzhiheng/PycharmProjects/untitled3')
df = pd.read_csv('test.csv', dtype=str, encoding='utf-8')
print(df.head(5))
'''
   name sex
0   jzz   0
1   zbb   1
2  jzzh   1
'''


# 使用函数对数据进行处理
def f(x):
	if '0' in str(x):
		return '女'
	elif '1' in str(x):
		return '男'
	else:
		return '无'


df['性别'] = df['sex'].apply(f)
print(df)
del df['性别']
df['名称'] = df['name'].apply(lambda x: str(x).replace(x[0:1], '**'))
print(df)
'''
   name sex 性别
0   jzz   0  女
1   zbb   1  男
2  jzzh   1  男
'''
df['性别'] = df['sex'].map({'0': '女', '1': '男'})
df['性别'] = df['sex'].map(f)
print(df)
'''
   name sex 性别
0   jzz   0  女
1   zbb   1  男
2  jzzh   1  男
'''
