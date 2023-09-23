import sqlite3
conn = sqlite3.connect('/Users/macbook/Documents/Python/Python/Advanced/lesson07/data.db')
c = conn.cursor()
c.execute('''
    create table bangSV(
          MaSinhVien int,
          TenSv varchar,
          NamSinh int,
          DiaChi varchar,
          Class varchar,
          LocationMathTest varchar,
          primary key(MaSinhVien)
    )
''')