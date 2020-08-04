import pandas as pd
import numpy as np

series1 = pd.Series([2.8, 3.01, 8.22, 9.66, 5.31])
print(type(series1))  # <class 'pandas.core.series.Series'>
print(series1)
'''
0    2.80
1    3.01
2    8.22
3    9.66
4    5.31
dtype: float64
'''
series2 = pd.Series([2.8, 3.01, 8.22, 9.66, 5.31], index=['a', 'b', 'c', 'd', 'e'], name='这是一个序列')
print(series2)
'''
a    2.80
b    3.01
c    8.22
d    9.66
e    5.31
Name: 这是一个序列, dtype: float64
'''
series3 = pd.Series({'a': 2.8, 'b': 3.01, 'c': 8.22, 'd': 9.66, 'e': 5.31})
print(series3)
'''
a    2.80
b    3.01
c    8.22
d    9.66
e    5.31
dtype: float64
'''
print(series3['a'])  # 2.8
print(series3[0:3])  # 通过位置访问是左闭右开的
'''
a    2.80
b    3.01
c    8.22
'''
print(series3['a':'d'])  # 通过标签访问则是左闭右闭
'''
a    2.80
b    3.01
c    8.22
d    9.66
'''
# 输出值
print(series3.values)  # [2.8  3.01 8.22 9.66 5.31]
print(series3.dtypes)  # float64

lst1 = [['张三', 23, '男'], ['李四', 27, '女'], ['王二', 26, '女']]  # 嵌套列表
df1 = pd.DataFrame(lst1, columns=['姓名', '年龄', '性别'])
print(df1.head(5))
'''
   姓名  年龄 性别
0  张三  23  男
1  李四  27  女
2  王二  26  女
'''
df2 = pd.DataFrame({'姓名': ['张三', '李四', '王二'], '年龄': [23, 27, 26], '性别': ['男', '女', '女']})
print(df2.head())
array1 = np.array([['张三', 23, '男'], ['李四', 27, '女'], ['王二', 26, '女']])
df3 = pd.DataFrame(array1, columns=['姓名', '年龄', '性别'], index=['a', 'b', 'c'])
print(df3.head())
print(df3.values)
print(df3.columns)  # Index(['姓名', '年龄', '性别'], dtype='object')
print(df3.dtypes)
''' 通过array创建的都是object
姓名    object
年龄    object
性别    object
dtype: object
'''
