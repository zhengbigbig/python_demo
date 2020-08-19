import pandas as pd
import os
import yagmail
from email.parser import Parser
import poplib
from email.header import decode_header

excel_path = '/Users/zhengzhiheng/PycharmProjects/untitled3/渠道数据分析总表.xlsx'

data = pd.read_excel(excel_path)

names = {
	'陈文': 'email'
}

dirname = 'exceldir'

if not os.path.exists(dirname):
	os.makedirs(dirname)

for name, email in names.items():
	df = data.loc[data['负责人'] == name]
	filepath = os.path.join(dirname, f'{name}.xlsx')
	writer = pd.ExcelWriter(filepath)
	df.to_excel(writer, 'Sheet1')
	writer.save()
	if email:
		# send email
		'''
		发送邮件
		'''
		# 登录SMTP服务器
		# user password host
		yag = yagmail.SMTP(user='', password='', host='smtp.sina.com')
		# 邮箱内容
		contents = [
			'hello',
			'world'
		]
		yag.send(to='780357902@qq.com', subject='标题', contents=contents)


def connect_email():
	'''
	接收邮件
	'''
	# useraccount - 邮箱账户
	# password - 邮箱登录授权码
	# pop3_server - 邮箱POP3服务器地址
	useraccount = ''
	password = ''
	pop3_server = 'pop.sina.com'
	# 开始连接到服务器
	server = poplib.POP3(pop3_server)
	# 打开或关闭调试信息
	server.set_debuglevel(1)
	# 打印POP3服务器的欢迎文字
	print(server.getwelcome().decode('utf8'))
	# 开始进行身份验证
	server.user(useraccount)
	server.pass_(password)
	return server


def get_email_content(server):
	'''返回邮箱中的最新电子邮件'''
	# 返回电子邮件总数目和占用服务器的空间大小
	email_num, email_size = server.stat()
	# 根据索引ID获取电子邮件的信息
	rsp, msglines, msgsize = server.retr(email_num)
	# 拼接电子邮件内容并对内容进行GBK解码
	msg_content = b'\r\n'.join(msglines).decode('gbk')
	# 把电子邮件内容解析为Message对象
	msg = Parser().parsestr(msg_content)
	# 关闭与服务器的链接，释放资源
	server.close()
	return msg


def parser_subject(msg):
	'''解析邮件主题'''
	subject = msg['Subject']
	# 解析邮件
	value, charset = decode_header(subject)[0]
	# 如果制定了字体集
	if charset:
		value = value.decode(charset)
	return value


def parser_content(msg, indent=0):
	'''有多个部分，对每个部分都进行解析'''
	if msg.is_multipart():
		parts = msg.get_payload()
		for n, part in enumerate(parts):
			print(f"{' ' * indent * 4} 第 {n + 1} 部分")
			print(f"{' ' * indent * 4} {'-' * 50}")
			parser_content(part, indent + 1)  # 递归解析
	else:
		content_type = msg.get_content_type().lower()
		if content_type == 'text/plain' or content_type == 'text/html':
			content = msg.get_payload(decode=True)
			charset = guess_charset(msg)  # 猜测字符集
			if charset:
				content = content.decode(charset)  # 解码
				print(f"{' ' * indent * 4} 邮件内容：{content}")
			else:
				print(f"{' ' * indent * 4} 附近内容：{content_type}")


def main():
	server = connect_email()
	msg = get_email_content(server)
	print(parser_subject(msg))
	parser_content(msg)


main()
