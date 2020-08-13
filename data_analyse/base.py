import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # 对matplotlib的封装
import os

os.chdir('/Users/zhengzhiheng/PycharmProjects/untitled3')

pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 100)

data = pd.read_csv('athlete_events.csv')
regions = pd.read_csv('noc_regions.csv')

merged = pd.merge(data, regions, on='NOC', how='left')
print(merged)
