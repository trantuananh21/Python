class SinhVien():
    def __init__(self):
        self.ma_sv = input('MaSinhVien: ')
        self.hoten =  input('Ho va Ten: ')
        self.tuoi = input('Tuoi: ')
        self.diem = input('Diem: ')

    def display(self):
        print(f'''
            Ma SV: {self.ma_sv}
            HoTen:  {self.hoten}
            Tuoi: {self.tuoi}
            Diem: {self.diem}
            ''')
    

sinh_vien_a = SinhVien()
sinh_vien_b = SinhVien()

print('Sinh vien A:')
sinh_vien_a.display()
print('Sinh vien B:')
sinh_vien_b.display()