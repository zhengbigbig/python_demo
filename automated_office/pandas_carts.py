import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir('/Users/zhengzhiheng/PycharmProjects/untitled3/myproject/automated_office')

people = pd.read_excel('people.xlsx', sheet_name='用户信息')
print(people, people.columns)
# sort_values 排序
people.sort_values(by='age', ascending=False, inplace=True)

# 直接使用 plt.bar() 绘制柱状图
plt.bar(people.name, people.age, color='orange')
# 设置标题，x轴名称与y轴名称，fontsize 设置字号
plt.title('people age', fontsize=16)
plt.xlabel('name')
plt.ylabel('age')

# 因为x轴字体太长，利用rotation将其旋转90度，方便显示
plt.xticks(people.name, rotation='90')
# 紧凑型布局，因为x轴文字比较长，为了让其显示全，使用紧凑型布局
plt.tight_layout()
plt.show()

# 如果需要显示中文，需要加字体
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"xxx.ttc", size=16)
plt.title('年龄梯度', fontproperties=font, fontsize=16)
plt.xlabel('姓名', fontproperties=font, fontsize=14)
plt.ylabel('年龄', fontproperties=font, fontsize=14)