import requests
import os
import json
import traceback
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

executor = ThreadPoolExecutor(10)
executor2 = ThreadPoolExecutor(10)
queue = Queue()


def get_http_session(pool_connections=2, poolmaxsize=10, max_retries=3):
	'''
	:param pool_connections:    要缓存的urllib3连接池的数量
	:param poolmaxsize: 最大连接数
	:param max_retries: 最大重试次数
	:return:
	'''
	session = requests.sessions()
	adapter = requests.adapters.HTTPAdapter(
		pool_connections=pool_connections,
		poolmaxsize=poolmaxsize,
		max_retries=max_retries
	)
	session.mount('https://', adapter)
	session.mount('http://', adapter)
	return session


def save_file(filepath, content):
	with open(filepath, 'w') as f:
		f.write(content)


def make_dir(name):
	up_dir = os.path.join(dir_path, name)
	if not os.path.exists(up_dir):
		os.makedirs(up_dir)
	return up_dir


def log(content, level, filepath):
	if level == 'error':
		with open(filepath, 'a') as f:
			f.write(content)
	elif level == 'fail':
		with open(filepath, 'a') as f:
			f.write(content)


def read_json(filepath):
	with open(filepath, 'r') as f:
		res = f.read()
	return json.loads(res)


def get_up_video_info(name, uid, filepath):
	res = read_json(filepath)
	vlist = res['data']['list']['vlist']
	for v in vlist:
		aid = v['aid']
		url = f'https://api.bilibili.com/x/player/pagelist?aid={aid}&jsonp=jsonp'
		player = get_http_session().get(url, timeout=10)
		player = player.json()
		data = player['data']
		if not data:
			return
		for d in data:
			try:
				get_video_comment_info(uid, aid)
			except Exception as e:
				log(traceback.format_exc(), 'error', 'base_info_fail.log')
				error_str = f'name: [{name}],uid:[{uid}], url: [{url}]'
				log(error_str, 'error', 'base_info_error.log')


def get_up_base_info(name, uid):
	try:
		url = f'https://api.bilibili.com/x/space/arc/search?mid={uid}&pn=1&ps=25&order=click&jsonp=jsonp'

		r = get_http_session().get(url, timeout=100)
		if r.status_code == 200:
			up_dir = make_dir(name)
			filepath = os.path.join(up_dir, f'{uid}_base_info.json')
			# 对json进行处理 indent 缩进 ensure_ascii 不进行编码
			content = json.dumps(r.json(), indent=4, ensure_ascii=False)
			save_file(filepath, content)
			# 将信息推到队列中
			global queue
			queue.put((name, uid, filepath))
			print('保存成功')
		else:
			# TODO 将失败的内容记录保存到Log中
			fail_str = f'name: [{name}],uid:[{uid}], url: [{url}]'
			log(fail_str, 'fail', 'base_info_error.log')

	except Exception as e:
		log(traceback.format_exc(), 'error', 'base_info_fail.log')
		error_str = f'name: [{name}],uid:[{uid}], url: [{url}]'
		log(error_str, 'error', 'base_info_error.log')


def base_info_task(power_json):
	for d in power_json:
		uid = d['uid']
		name = d['name']
		# 通过线程池执行
		executor.submit(get_up_base_info, name, uid)


def video_info_task():
	with ThreadPoolExecutor(max_workers=10) as executor:
		while True:
			global queue
			name, uid, filepath = queue.get()
			executor.submit(get_up_video_info, name, uid, filepath)
			queue.task_done()
			time.sleep(2)


def main():
	power_up = read_json('power_up_100.json')
	get_up_base_info(power_up)
	Thread(target=base_info_task, args=(power_json,)).start()
	Thread(target=video_info_task).start()


if __name__ == '__main__':
	main()
