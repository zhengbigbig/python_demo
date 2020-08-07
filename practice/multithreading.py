import time
import threading
from multiprocessing import Process


def longtime():
	time.sleep(5)


# 开启一个线程来使用longtime
t = threading.Thread(target=longtime, name='longtime_thread')
t.start()

if __name__ == '__main__':
	# 开启一个进程使用longtime
	p = Process(target=longtime)
	p.start()
