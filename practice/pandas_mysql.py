import pandas as pd
import pymysql
from sqlalchemy import create_engine
import os


def create_connection(**kwargs):
	try:
		host = kwargs.get('host')
		user = kwargs.get('user')
		password = kwargs.get('password')
		database = kwargs.get('database')
		port = kwargs.get('port')
		url = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database)
		connection = create_engine(url)
		print('Connection to MySQL DB successful.')
		return connection
	except Error as e:
		print(f"The error '{e}' occurred.")


def query(conn, query_sql):
	try:
		result = pd.read_sql(query_sql, con=conn)
		return result
	except Error as e:
		print(f"search fail {e}")


connect = create_connection(
	user='root', password='root', host='localhost', port=3306, database='test')
sql = '''select * from users;'''
result = query(conn=connect, query_sql=sql)
print(result)

path = os.path.abspath(os.path.join(os.getcwd(), './test.csv'))
print(path)
df = pd.read_csv(path, encoding='utf-8')
print(df)
try:
	df.to_sql('users', con=connect, index=False, if_exists='replace')
except:
	print('error')
