from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import requests

CHROMEDRIVER = '/Users/zhengzhiheng/PycharmProjects/untitled3/myproject/crawler2/chromedriver'

# 1. 创建浏览器对象
driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
# 2. 发送请求
driver.get('https://bbs.tianya.cn/#')

# 3. 找到标签为情感的
wait = WebDriverWait(driver, 20)
target_li = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, '情感')))
print(target_li.text)
target_li.click()
time.sleep(3)


# 4. 滚动加载所有的数据
def scroll_to_bottom(dr):
	# 获取到当前窗口总高度JS
	js = "return action=document.body.scrollHeight"
	# 初始化滚动条的高度为0
	height = 0
	# 当前窗口总高度
	new_height = dr.execute_script(js)

	while height < new_height:
		# 将滚动条调整至页面底部
		for i in range(height, new_height, 100):
			dr.execute_script('window.scrollTo(0, {})'.format(i))
		height = new_height
		time.sleep(2)
		new_height = dr.execute_script(js)


scroll_to_bottom(driver)

# 5. 找到所需内容
ul = driver.find_element_by_xpath("//div[@class='bbsbox']/ul")
target_lst = ul.find_elements_by_css_selector("li")
print(len(target_lst))

for index, li in enumerate(target_lst):
	a_title = li.find_element_by_css_selector("h2 > a")
	title = a_title.get_attribute("title")
	href = a_title.get_attribute("href")
	summary = ''
	try:
		content = li.find_element_by_class_name("summary")
		summary = content.text
	except NoSuchElementException:
		summary = ''

	other = li.find_element_by_class_name("info")
	author = other.find_element_by_css_selector("span.author > a").text
	region = other.find_element_by_css_selector("span.from > a").text

	print(index, title, href, summary, author, region)

driver.quit()
