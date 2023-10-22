import sqlite3

conn = sqlite3.connect('/Users/macbook/Documents/Python/Python/Advanced/SPCK/benh_vien.db')
cur = conn.cursor()
# cur.execute('''
#             create table BacSi(
#             ID int,
#             HoTen varchar,
#             NamSinh int,
#             DiaChi varchar,
#             Email varchar,
#             HSL numeric,

#             primary key(ID)

# )
# ''') 

# cur.execute('''
#             create table BenhNhan(
#             ID int,
#             HoTen varchar,
#             NamSinh int,
#             DiaChi varchar,
#             Khoa varchar,
#             Benh varchar,
#             NgayNhapVien text,
#             NgayXuatVien text,
#             SoPhong int,
#             DonThuoc text,

#             primary key(ID)

# )
# ''') 

# cur.execute('''
#             create table Thuoc(
#             ID int,
#             Ten varchar,
#             ChucNang varchar,
#             NSX text,
#             HSD text,
#             SoLuong int,

#             primary key(ID)

# )
# ''') 
conn.close()