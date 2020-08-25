import requests
from requests.adapters import HTTPAdapter


def get_http_session(pool_connections=2, pool_maxsize=10, max_retries=3):
	'''
	http 连接池，减少资源的浪费
	:param pool_connections:    要缓存的urllib3连接池的数量
	:param poolmaxsize: 最大连接数
	:param max_retries: 最大重试次数
	:return:
	'''
	session = requests.session()
	adapter = requests.adapters.HTTPAdapter(
		pool_connections=pool_connections,
		pool_maxsize=pool_maxsize,
		max_retries=max_retries
	)
	session.mount('https://', adapter)
	session.mount('http://', adapter)
	return session
