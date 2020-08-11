from bs4 import BeautifulSoup
import requests
import os
import time

os.chdir('/Users/zhengzhiheng/PycharmProjects/untitled3')
download_path = './douban'
if not os.path.exists(download_path):
	os.makedirs(download_path)

base_target = 'https://movie.douban.com/top250'


def download_pic(url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
	res = requests.get(url, headers=headers)
	soup = BeautifulSoup(res.text, 'lxml')  # 将网页内容指定解析器来解析
	content = soup.find('div', class_='article')
	images = content.find_all('img')  # 获取所有图片的标签
	pic_link_list = [image['src'] for image in images]  # 所有图片的下载链接
	pic_name_list = [image['alt'] for image in images]  # 所有电影名称
	for name, link in zip(pic_name_list, pic_link_list):  # 下载内容到本地
		html = requests.get(link)
		with open(f'{download_path}/{name}.jpg', 'wb') as f:
			f.write(html.content)


def main():
	start_urls = [base_target]
	for i in range(1, 10):
		start_urls.append(f'{base_target}?start={25 * i}&filter=')

	start_time = time.time()
	for url in start_urls:
		download_pic(url)
	end_time = time.time()
	print('-' * 50)
	print(f'运行时间：{end_time - start_time}')


if __name__ == '__main__':
	main()
