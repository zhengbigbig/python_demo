import pandas as pd
import numpy as np
import os

os.chdir('/Users/zhengzhiheng/PycharmProjects/untitled3')
df = pd.read_csv('test.csv', dtype=str, encoding='utf-8')
print(df)
grouped = df.groupby(by=['sex'])
print(grouped)  # pandas.core.groupby.generic.DataFrameGroupBy
print(grouped.sum()['visit'])

