import xlrd
import os
import pandas as pd

os.chdir('/Users/zhengzhiheng/PycharmProjects/untitled3')
wordbook = xlrd.open_workbook('test.xlsx')
sheet_name = wordbook.sheet_names()
print(sheet_name)
lst = pd.read_excel('test.xlsx', sheet_name=0)
lst2 = pd.read_excel('test.xlsx', sheet_name=1)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 100)
print(lst.head(5))
# ignore_index 索引重置
print(pd.concat([lst, lst2], axis=0, ignore_index=True))
# 也可以使用遍历合并
basic = pd.DataFrame()
for i in sheet_name:
	basic_i = pd.read_excel('test.xlsx', sheet_name=i)
	basic = pd.concat([basic, basic_i], axis=0, ignore_index=True)
print(basic)
# 关联表
df = pd.read_csv('users.csv', dtype={'user_id': str})
df2 = pd.read_csv('order.csv', dtype={'user_id': str})
df3 = pd.merge(left=df, right=df2, how='inner', left_on='user_id', right_on='user_id')
print(df3)
