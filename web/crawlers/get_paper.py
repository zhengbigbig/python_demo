import requests
from bs4 import BeautifulSoup
import traceback
import csv
from myproject.web.utils.requests import get_http_session


def get_papers(skip):
	try:
		url = f'https://arxiv.org/list/cs/pastweek?skip={skip}&show=100'
		headers = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'

		}
		# 代理
		proxies = {
			'http': 'http://127.0.0.1:1087',
			'https': 'http://127.0.0.1:1087',
		}
		res = get_http_session().get(url, headers=headers)
		if res.status_code != 200:
			return False, '请求网页失败'
		print(res, '*' * 10)
		# pip install lxml
		soup = BeautifulSoup(res.text, 'lxml')  # lxml 解析速度快
		all_dt = soup.find_all('dt')
		all_dd = soup.find_all('dd')

		for dt, dd in zip(all_dt, all_dd):
			url = dt.find(class_='list-identifier').find('a').get('href')
			root_url = 'https://arxiv.org'
			full_url = root_url + url

			title = dd.find(class_='list-title mathjax').contents
			if len(title) >= 3:
				title = title[2]
			else:
				title = dd.find(class_='list-title mathjax').text

			authors = dd.find(class_='list-authors').text
			authors = authors.split(':')[1].replace('\n', '')

			yield title, full_url, authors

	except Exception as e:
		print(e)
		traceback.print_exc()


def main():
	resl = []
	for i in range(0, 1442, 100):
		for title, full_url, authors in get_papers(i):
			resl.append([title, full_url, authors])
			print(title, 'done!')
	with open('papers.csv', 'w') as f:
		cw = csv.writer(f)
		for i in resl:
			# 写一行
			cw.writerow(i)


if __name__ == '__main__':
	main()
