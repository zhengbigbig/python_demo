import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')
import json

movie = pd.read_csv('/Users/zhengzhiheng/PycharmProjects/untitled3/tmdb_5000_movies.csv')
credit = pd.read_csv('/Users/zhengzhiheng/PycharmProjects/untitled3/tmdb_5000_credits.csv')
print(movie.columns)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 100)


def json2list(target, name):
	target[name] = target[name].apply(json.loads)
	for index, i in zip(target.index, target[name]):
		lst = []
		for _ in i:
			lst.append(_['name'])
		target.loc[index, name] = str(lst)


j2l = ['genres', 'keywords', 'production_companies', 'spoken_languages']
for _ in j2l:
	json2list(movie, _)

j2l2 = ['cast', 'crew']
for _ in j2l2:
	json2list(credit, _)
all_df = pd.merge(movie, credit, left_on='id', right_on='movie_id', how='left')

all_df.rename(columns={'title_x': 'title'}, inplace=True)
all_df.drop('title_y', axis=1, inplace=True)
# print(all_df.head(5))

# 1. 数据量最多的前10种电影类型
all_df['genres'] = all_df['genres'].str.strip('[]').str.replace(' ', '').str.replace("'", "")
all_df['genres'] = all_df['genres'].str.split(',')
genres_lst = []
for i in all_df['genres']:
	genres_lst.extend(i)
gen_lst = pd.Series(genres_lst).value_counts()[:10].sort_values(ascending=False)
gen_df = pd.DataFrame(gen_lst)
gen_df.rename(columns={0: 'Total'}, inplace=True)
print(gen_df)
plt.subplots(figsize=(10, 8))
sns.barplot(y=gen_df.index, x='Total', data=gen_df, palette='GnBu_d')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Total', fontsize=12)
plt.ylabel('Genres', fontsize=12)
plt.title('Top 10 genres', fontsize=12)
plt.show()

# 2. 不同电影类型和时间的关系
lst = list(set(genres_lst))
print(lst[:5])
print(all_df['genres'])