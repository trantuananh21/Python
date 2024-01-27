class SinhVien():
    def __init__(self, ten, nam_sinh, dia_chi, que, diem_toan, diem_ly, diem_hoa):
        self.ten = ten
        self.nam_sinh = nam_sinh
        self.dia_chi = dia_chi
        self.que = que
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa
    
    def aver_grade(self):
        grade = (self.diem_toan + self.diem_ly + self.diem_hoa) / 3
        return grade
    
    def filter(self):
        grade = (self.diem_toan + self.diem_ly + self.diem_hoa) / 3
        if grade >= 8.0 and self.diem_hoa > 6.5 and self.diem_ly > 6.5 and self.diem_toan > 6.5:
            print('Gioi')
        
        elif grade >= 6.5 and self.diem_hoa > 5.0 and self.diem_ly > 5.0 and self.diem_toan > 5.0:
            print('Kha')

        elif grade >= 5.0 and self.diem_hoa > 4.0 and self.diem_ly > 4.0 and self.diem_toan > 4.0:
            print('Trung binh')
        
        else:
            print('Yeu')

sv01 = SinhVien('Nguyen Van B', 2007, 'Ha Noi', 'Thai Binh', 6, 9, 7)
print(sv01.aver_grade())
sv01.filter()