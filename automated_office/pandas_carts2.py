import pandas as pd
import matplotlib.pyplot as plt

users = pd.read_excel('people.xlsx')

# 新计算一个总量，用于排序
users['Total'] = users['Jan'] + users['Feb'] + users['Mar']
# 排序
users.sort_values(by='Total', inplace=True)
# 水平叠加柱状图，barh中的h表示 horizontal水平的
# 使用 stacked 就可以实现叠加形式
users.plot.barh(x='Name', y=['Jan', 'Feb', 'Mar'], stacked=True)
plt.tight_layout()
plt.show()
