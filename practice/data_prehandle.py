import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/Users/zhengzhiheng/PycharmProjects/untitled3')
df = pd.read_csv('test.csv', dtype=str, encoding='utf-8')
print(df.head(5))
'''
   name sex    asset visit
0   jzz   0  $19,300     1
1   zbb   1  $17,200    45
2  jzzh   1   $1,000     5
3  jzzh   1   $1,000     5
'''


def f(x):
	if '$' in str(x):
		x = str(x).strip('$')
		x = str(x).replace(',', '')
	else:
		x = str(x).replace(',', '')
	return float(x)


df['asset'] = df['asset'].apply(f)
print(df)
'''
   name sex    asset visit
0   jzz   0  19300.0     1
1   zbb   1  17200.0    45
2  jzzh   1   1000.0     5
3  jzzh   1   1000.0     5
'''
# 重复值处理
print(df.duplicated())  # 查看是否有重复数据
'''
0    False
1    False
2    False
3     True
dtype: bool
'''
print(any(df.duplicated()))  # True 有一个重复则True
print(np.sum(df.duplicated()))  # 1 统计重复个数
print(df.drop_duplicates(inplace=False))  # 删除重复数据 inplace 是否改变原有的数据
'''
   name sex    asset visit
0   jzz   0  $19,300     1
1   zbb   1  $17,200    45
2  jzzh   1  $11,000     5
3  jzzh   1  $11,000   NaN
4   zzz   1       $2     6
'''
print(df.drop_duplicates(subset=['name']))  # 对指定的值去重

# 缺失值处理
# 统计每一行的缺失
print(df.apply(lambda x: sum(x.isnull()) / len(x), axis=0))
'''
name     0.00
sex      0.00
asset    0.00
visit    0.25
dtype: float64
'''
# 缺失值删除  all 都是缺失值时删除，any有缺失值时删除
df.dropna(how='any', subset=['visit'], axis=0, inplace=False)
print(df)
# 缺失值填补
df.fillna(0)
# 有缺失的用均值填补
# 使用出现频率最高的填补
df['visit'].fillna(df['visit'].mode()[0], inplace=True)
print(df)
df.fillna(value={'visit': 1})
# ffill 前项填补，bfill 后项填补
df['visit'].fillna(method='bfill')

# 异常值处理
x_bar = df['asset'].mean()
print(x_bar)  # 均值
x_std = df['asset'].std()  # 标准差
print(x_std)
print(any(df['asset'] > x_bar + 2 * x_std))  # False
print(any(df['asset'] < x_bar - 2 * x_std))  # False
Q1 = df['asset'].quantile(q=0.25)
Q2 = df['asset'].quantile(q=0.75)
IQR = Q2 - Q1
print(any(df['asset'] > Q2 + 1.5 * IQR))

print(df['asset'].plot(kind='box'))
plt.show()

# 盖帽法处理
P99 = df['asset'].quantile(q=0.99)
P1 = df['asset'].quantile(q=0.01)
df['new_asset'] = df['asset']
df.loc[df['asset'] > P99, 'new_asset'] = P99
df[['asset', 'new_asset']].describe()
# 数据离散化
df['n_asset'] = pd.cut(df['asset'], 5, labels=range(5))
print(df)
df['n_asset'].value_counts().plot(kind='bar')
plt.show()
w = [0, 100, 1000, 10000, 100000]
df['c_asset'] = pd.cut(df['asset'], bins=w, labels=range(4))
print(df)
df['c_asset'].hist()
plt.show()
k = 5
w = [1.0 * i / k for i in range(k + 1)]
df['c_asset'] = pd.qcut(df['asset'], q=w, labels=range(5))
df['c_asset'].hist()
