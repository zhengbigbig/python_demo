from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests

CHROMEDRIVER = '/Users/zhengzhiheng/PycharmProjects/untitled3/myproject/crawler2/chromedriver'

# 1. 创建浏览器对象
# driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
# 2. 发送请求
# driver.get('https://www.baidu.com')

# 模拟搜索操作
# input = driver.find_element_by_id('kw')
# input.clear()
# input.send_keys('CSDN')
# input.send_keys(Keys.ENTER)

name = 'ant-design/ant-design-pro'

api = 'https://apis.github.com/repos/' + name
weburl = 'https://github.com/' + name

old_time = None
while True:
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
	r = requests.get(api, headers=headers)
	if r.status_code != 200:
		print('请求API失败')
		break
	'''
		判断项目是否更新
	'''
	# json -> dict
	now_time = r.json()['updated_at']
	if not old_time:
		old_time = now_timesel
	if old_time < now_time:
		print('项目更新了')
		driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
		driver.get(weburl)
	time.sleep(600)
