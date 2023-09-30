import sqlite3

conn = sqlite3.connect('/Users/macbook/Documents/Python/Python/Advanced/lesson08/data.db')
con = conn.cursor()
con.execute('''
create table bangSV(
          ID int,
          HoTen varchar,
          Tuoi int,
          DiemVan int,
          DiemToan int,
          DiemAnh int,
        DiemTB int
          primary key(ID)
    )
''')
conn.close()