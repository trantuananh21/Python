import sqlite3

conn = sqlite3.connect('/Users/macbook/Documents/Python/Python/Advanced/lesson10/data.db')
cur = conn.cursor()
cur.execute('''
create table SanPham(
            ID int,
            Ten varchar,
            NamSanXuat int,
            DiaChiSanXuat varchar,
            Gia int,
            SoLuong int,
            
            primary key(ID)
)
''')
conn.close()