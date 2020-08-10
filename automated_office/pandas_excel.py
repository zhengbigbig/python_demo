import pandas as pd
import os

os.chdir('/Users/zhengzhiheng/PycharmProjects/untitled3/myproject/automated_office')
# DataFrame 数据帧 相当于工作簿中的一个工作表
df = pd.DataFrame({
	'id': [1, 2, 3],
	'name': ['x', 'y', 'z'],
	'age': [22, 13, 45]
})
# 自定义索引，不然pandas会使用默认的索引，这回导致生成的工作表也会有这些索引
df = df.set_index('id')
print(df)
df.to_excel('people.xlsx', sheet_name='用户信息', index=True, encoding='utf-8')
message = pd.read_excel('people.xlsx', sheet_name='用户信息')
print(message, message.columns)
# 排序
message.sort_values(by='age', ascending=False, inplace=True)
print(message)
message.to_excel('people.xlsx', sheet_name='用户信息', index=True, encoding='utf-8')