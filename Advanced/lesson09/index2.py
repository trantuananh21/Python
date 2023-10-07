import sqlite3

conn = sqlite3.connect('/Users/macbook/Documents/Python/Python/Advanced/lesson09/data2.db')
c = conn.cursor()
c.execute('''
create table bangSinhVien(
          ID int,
          Ten varchar,
          DiaChi varchar,
          NamSinh int,
          DiemToan int,
          DiemLy int,
          DiemHoa int,
          primary key(ID)
)
''')
conn.close()