import sqlite3

conn = sqlite3.connect('/Users/macbook/Documents/Python/Python/Advanced/lesson08/data2.db')
c = conn.cursor()
c.execute("""
create table bangSV(
          ID int,
          HoTen varchar,
          Tuoi int,
          DiemToan int,
          DiemVan int,
          DiemAnh int,
          primary key(ID)
    )
"""
)
conn.close()