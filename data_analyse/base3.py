import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

import os

dirpath = '/Users/zhengzhiheng/PycharmProjects/untitled3'
data = pd.read_csv(os.path.join(dirpath, 'athlete_events.csv'))
regions = pd.read_csv(os.path.join(dirpath, 'noc_regions.csv'))
merged = pd.merge(data, regions, on='NOC', how='left')
# 过滤出金牌的数据
goldMedals = merged[(merged.Medal == 'Gold')]
print(goldMedals.head(5))
# 绘制分布图
print(goldMedals.isnull().any())
# 过滤掉年龄为null的
goldMedals = goldMedals[np.isfinite(goldMedals['Age'])]
print(goldMedals.head(5))
# 绘制获得金牌的年龄分布
plt.figure(figsize=(20, 10))  # 画布大小
plt.tight_layout()  # 紧凑型布局
sns.countplot(goldMedals['Age'])
plt.title('ff')
plt.show()
# 绘制50岁以上获得金牌的项目
print(goldMedals['ID'][goldMedals['Age'] > 50].count())
plt.figure(figsize=(20, 10))  # 画布大小
plt.tight_layout()  # 紧凑型布局
sns.countplot(goldMedals['Sport'][goldMedals['Age'] > 50])
plt.title('ff')
plt.show()

# 绘制女子田径数据
womanonly_df = merged[(merged.Sex == 'F') & (merged.Season == 'Summer')]
print(womanonly_df.head())
# 绘制柱状图 夏季奥运会女子奖牌 变化
# x轴：年份 y轴：奖牌数
sns.set(style='darkgrid')
plt.figure(figsize=(20, 10))
sns.countplot(x='Year', data=womanonly_df)
plt.title('www')
plt.show()

# 绘制奖牌获得者和身高体重的分析
notnullMedals = merged[(merged['Height'].notnull()) & (merged['Weight'].notnull())]
print(notnullMedals.head())
plt.figure(figsize=(20, 10))
sns.scatterplot(x='Height', y='Weight', data=notnullMedals)
plt.title('yyy')
plt.show()

# 奥运会随时间的变化
# 男运动员数量变化(夏季运动会)
MenOverTime = merged[(merged.Sex == 'M') & (merged.Season == 'Summer')]
part = MenOverTime.groupby('Year')['Sex'].value_counts()
plt.figure(figsize=(12, 8))
part.loc[:, 'M'].plot()
plt.show()
# 年龄的变化
plt.figure(figsize=(20,10))
sns.boxplot('Year','Age',data=MenOverTime)
plt.show()
# 体重身高的变化
plt.figure(figsize=(20,10))
sns.pointplot('Year','Weight',data=MenOverTime)
plt.show()
