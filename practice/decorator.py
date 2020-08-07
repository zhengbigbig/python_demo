# 装饰器
def log(func):
	def wrapper(*args, **kwargs):
		print("log func {}".format(func.__name__))
		print(type(args), args)
		print(type(kwargs), kwargs)
		return func(*args, **kwargs)

	return wrapper


@log
def print_func(*args, **kwargs):
	print("this is func")


print_func(1, 2, 3, a=1, b=2, c=3)
'''
log func print_func
<class 'tuple'> (1, 2, 3)
<class 'dict'> {'a': 1, 'b': 2, 'c': 3}
this is func
'''


def logs(level):
	def decorator(func):
		def wrapper(*args, **kwargs):
			if level == 'info':
				print('info')
			elif level == 'error':
				print('error')
			return func(*args, **kwargs)

		return wrapper

	return decorator


@logs(level='error')
def print_logs():
	print('start')


print_logs()


# 类装饰器
class LogCls(object):
	def __init__(self, func):
		self.func = func

	def __call__(self, *args, **kwargs):
		print('logloglog')
		self.func(*args, **kwargs)


@LogCls
def print_log_cls():
	print('log_cls')


print_log_cls()
