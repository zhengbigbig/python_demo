import csv
from myproject.web.models.mysql import db
import time


def get_csv_info(path='/Users/zhengzhiheng/PycharmProjects/untitled3/papers.csv'):
	csvfile = open(path, 'r')
	reader = csv.reader(csvfile)
	for item in reader:
		yield item


def get_insert_sql():
	items = []
	_time = int(time.time())
	for item in get_csv_info():
		item = [db.escape_string(_) for _ in item]
		items.append(f"('{item[0]}','{item[1]}','{item[2]}','{_time}','{_time}')")

	values = ','.join(items)
	print(values)
	sql = f'''
	INSERT INTO
		papers (`title`,`url`,`authors`,`create_time`,`update_time`)
		values {values}
	'''
	row_id = db.insert(sql)
	print(f'{row_id}条数据插入完成')


if __name__ == '__main__':
	get_insert_sql()
