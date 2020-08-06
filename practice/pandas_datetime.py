import numpy as np
import pandas as pd
import os

os.chdir('/Users/zhengzhiheng/PycharmProjects/untitled3')
df = pd.read_excel('test.xlsx')
df['time'] = pd.to_datetime(df['操作时间'], format='%Y%m%d', errors='coerce')
print(df.head(5))
print(df.info())
print(df['time'].dt.year)
df['diff_day'] = pd.datetime.now() - df['time']
# 类型必须是timedalta
# 显示时间差的天数
print(df['diff_day'].dt.days)
# 转化为天数 D 小时 H 分钟 M
df['时间差'] = df['diff_day'] / pd.Timedelta('1 D')
print(df['时间差'].round(decimals=3))
# 转为天数 D 月数 M  年 Y 时 H 等
print(df['diff_day'].astype('timedelta64[Y]'))
