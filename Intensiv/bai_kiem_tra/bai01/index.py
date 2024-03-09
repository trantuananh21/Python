class SinhVien():
    def __init__(self, ten, maso, tuoi, diem_trung_binh):
        self.ten = ten
        self.maso = maso
        self.tuoi = tuoi
        self.diem_trung_binh = diem_trung_binh

    def print_info(self):
        print(f'''
Ho va Ten: {self.ten}
Ma so sinh vien: {self.maso}
Tuoi: {self.tuoi}
Diem trung binh: {self.diem_trung_binh}
''')
    
    
        
sv01 = SinhVien('Nguyen Van A', 1, 20, 7.8)
sv02 = SinhVien('Tran Tuan Z', 2, 21, 10.0)

# Hiện thị thông tin sinh viên
sv01.print_info()
sv02.print_info()

# Tìm kiếm sinh viên theo mã số
# SELECT * FROM SinhVien WHERE Maso = 1

# Xoá thông tin sinh viên
# DELETE FROM SinhVien WHERE Maso = 2

# Em không làm kịp ạ