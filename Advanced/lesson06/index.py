# Cơ sở dữ liệu là nơi để lưu trữ dữ liệu

import sqlite3
conn = sqlite3.connect('/Users/macbook/Documents/Python/Python/Advanced/lesson06/data.db')
c = conn.cursor()
c.execute('''
    create table employ_info(
          employ_id int,
          first_name varchar,
          last_name varchar,
          primary key(employ_id)
    )
''')