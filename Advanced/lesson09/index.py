import sqlite3

conn = sqlite3.connect('/Users/macbook/Documents/Python/Python/Advanced/lesson09/data.db')
c = conn.cursor()
c.execute('''
    create table bangSV(
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