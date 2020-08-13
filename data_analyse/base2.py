import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # 对matplotlib的封装
import os

os.chdir('/Users/zhengzhiheng/PycharmProjects/untitled3')

pd.set_option('display.max_columns', 20)

lc = pd.DataFrame(pd.read_excel('20191217083259_72842.xlsx'))
# lc.set_index('专业要求', drop=True, inplace=True)
print(lc.columns)
data = lc.loc[((lc['专业要求'] == '不限')
               | (lc['专业要求'].str.find('园林') != -1)
               | (lc['专业要求'].str.find('农业类') != -1)
               | (lc['专业要求'].str.find('林业类') != -1)
               | (lc['专业要求'].str.find('环境保护类') != -1)
               | (lc['专业要求'].str.find('城建规划类') != -1)
               | (lc['专业要求'].str.find('建筑工程类') != -1))
				 & (lc['性别要求'] == '不限')& (lc['现有身份要求'] == '不限')]
data2 = data.loc[lc['户籍要求'] == '不限']
print(data)
data.to_excel('test.xlsx', sheet_name='test', index=True, encoding='utf-8')
print('招聘类数：{}，满足要求但户籍限制的类数：{}，满足要求无户籍限制类数：{}'.format(lc['专业要求'].count(), data['专业要求'].count(),data2['专业要求'].count()))
