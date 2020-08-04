
import pandas as pd
import numpy as np
import os
path = os.path.abspath(os.path.join(os.getcwd(), './csvfile.csv'))
baby = pd.read_csv(path, encoding='utf-8')
order = pd.read_csv('order.csv', encoding='gbk', dtype={'info_id': str})
order.info()  # 输出信息
history = pd.read_csv('history.csv', nrows=100)  # 显示一百行
# 设置显示行和列
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 100)
# 保存csv
baby.to_csv('test.csv', encoding='utf-8', index=False)  # index是否保存到csv
