import pandas as pd

df = pd.read_excel('order.xlsx', sheet_name=0)  # sheet_name 可以是工作页的名称也可以是索引
df1 = pd.read_excel('order.xlsx', encoding='utf-8', nrows=10)
df.to_excel('n_order.xlsx', sheet_name='sheet1', index=False, encoding='utf-8')
