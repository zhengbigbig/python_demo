import xlrd
import os
import pandas as pd
import numpy as np

os.chdir('/Users/zhengzhiheng/PycharmProjects/untitled3')
df = pd.read_excel('test.xlsx', sheet_name=0)
print(df)
# grouped = df.groupby('weekday')
# print(grouped.agg([np.mean, np.max, np.min]))
# print(grouped.agg({'total_item': np.mean, 'count': np.max}))
# print(df[['total_item', 'count']].agg(np.sum, np.mean, np.max))

print(df.columns)
# 缺失值填补
pd.pivot_table(data=df, index='weekday', values='total_items',
               aggfunc=[np.mean, np.sum], margins=True,
               margins_name='总计', fill_value=0)
# normalize 除以总的数量
pd.crosstab(index=df['weekday'], columns=df['discount'], margins=True, normalize='all')
