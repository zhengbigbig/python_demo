# coding:utf-8
import re
import json
from datetime import datetime
import pandas as pd
import requests

url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

page = requests.get(url).content.decode('utf-8')

regexp = "<script id=\"getListByCountryTypeService2true\">([^<]+)"
res = re.findall(regexp, page)

data = res[0][48:-11]
dicts = json.loads(data)
n_dicts = []
for row in dicts:
	for key in row:
		if key in ['createTime', 'modifyTime']:
			date_time = datetime.fromtimestamp(row[key] / 1000).strftime("%Y-%m-%d %H:%M:%S")
			row[key] = date_time
df = pd.DataFrame(dicts)
df.to_csv("ncov1.csv", mode="a")
