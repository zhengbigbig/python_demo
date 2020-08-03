import sqlite3
import os

path = os.path.abspath(os.path.join(os.getcwd(), "./myproject/sm_app.sqlite"))
print(path)
conn = sqlite3.connect(path)

cur = conn.cursor()

create_users_table = """
create table if not exists users
(
  id     integer primary key autoincrement,
  name   text not null,
  age    integer,
  gender text
);
"""

insert_user = """
insert into users (name, age, gender)
values ('zbb', 18, 'man'),('zbb', 18, 'man');
"""

cur.execute(create_users_table)
cur.execute(insert_user)
conn.commit()  # 对数据库的增删改需要提交

select_users = """
select * from users;
"""
cur.execute(select_users)
result = cur.fetchall()
print(result)
# 执行完毕
cur.close()
conn.close()
