'''
列表生成表达式
'''
l = [i for i in range(10) if i % 2 == 0]
print(l)  # [0, 2, 4, 6, 8]
# 与上述写法等价
l = []
for i in range(10):
	if i % 2 == 0:
		l.append(i)
'''
字典生成表达式
'''
d = {i: i + 10 for i in range(10)}
print(d)  # {0: 10, 1: 11, 2: 12, 3: 13, 4: 14, 5: 15, 6: 16, 7: 17, 8: 18, 9: 19}
# 与上述写法等价
d = {}
for i in range(10):
	d[i] = i + 10

'''
生成器表达式
'''
g = (i for i in range(10))
# 返回生成器
print(g) # <generator object <genexpr> at 0x1083fdc78>
print('使用__next__')
print(g.__next__())
print('通过循环打印生成器中的值')
for i in g:
	print(i)
