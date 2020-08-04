import mysql.connector
from mysql.connector import Error


# 连接mysql
def create_connection(host_name, user_name, user_password, db_name):
	connection = None
	try:
		connection = mysql.connector.connect(
			host=host_name,
			user=user_name,
			password=user_password,
			database=db_name
		)
		print('Connection to MySQL DB successful.')
	except Error as e:
		print(f"The error '{e}' occurred.")
	return connection


# 连接
connection = create_connection("localhost", "root", "root", "TEST")


# 建表，即：写
def execute_query(connection, query):
	cursor = connection.cursor()
	try:
		cursor.execute(query)
		connection.commit()
		print('Query executed successfully.')
	except Error as e:
		print(f"The error '{e}' occurred.")


create_users_table = """
create table if not exists users (
  id   int auto_increment,
  name   text not null,
  age    int ,
  gender text,
  primary key (id)
) ENGINE = InnoDB;
"""
insert_user = """
insert into users (name, age, gender)
values ('zbb', 18, 'man'),('zbb', 18, 'man');
"""
select_users = """
select * from users;
"""
execute_query(connection, create_users_table)
execute_query(connection, insert_user)


# 查询函数，即：读
def execute_read_query(connection, query):
	cursor = connection.cursor()
	result = None
	try:
		cursor.execute(query)
		result = cursor.fetchall()
		return result
	except Error as e:
		print(f"The error '{e}' occurred.")


print(execute_read_query(connection, select_users))
