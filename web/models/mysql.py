import pymysql
import logging


class MySQLDB(object):
	def __init__(self, host='localhost', port=3306, user='root', password='root', db='test'):
		# cursorclass=pymysql.cursors.DictCursor 数据库查询返回dict --> 默认：tuple
		self.conn = pymysql.connect(
			host=host, port=port, user=user, password=password, db=db,
			charset='utf8', cursorclass=pymysql.cursors.DictCursor)
		self.log = logging.getLogger(__name__)

	def execute(self, sql, kwargs):
		try:
			cursor = self.conn.cursor()
			cursor.execute(sql, kwargs)
			self.conn.commit()  # 插入、删除commit 、 查询
			return cursor
		except Exception as e:
			self.log.error(f'mysqldb execute error :{e}', exc_info=True)
			raise e

	def query(self, sql, kwargs=None):
		cursor = None
		try:
			cursor = self.execute(sql, kwargs)
			if cursor:
				return cursor.fetchall()  # 查询所有内容，dict
			else:
				raise Exception(f'sql error: {sql}')
		except Exception as e:
			self.log.error(e)
			raise e
		finally:
			if cursor:
				cursor.close()

	def insert(self, sql, kwargs=None):
		cursor = None
		try:
			cursor = self.execute(sql, kwargs)
			if cursor:
				row_id = cursor.lastrowid
				return row_id
			else:
				raise Exception(f'sql error: {sql}')
		except Exception as e:
			self.log.error(e)
			raise e
		finally:
			if cursor:
				cursor.close()

	# 对数据进行转码
	def escape_string(self, _):
		return pymysql.escape_string(_)


db = MySQLDB(user='root', password='root', db='test')
