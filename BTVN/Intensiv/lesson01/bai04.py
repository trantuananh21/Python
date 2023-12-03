class Student():
    def __init__(self, ten, diem_toan, diem_van, diem_anh):
        self.ten = ten
        self.diem_toan = diem_toan
        self.diem_van = diem_van
        self.diem_anh = diem_anh

    def getAverGrade(self):
        sum_grade = self.diem_anh + self.diem_toan + self.diem_van
        aver = sum_grade / 3
        return aver
    
    def getAbility(self):
        sum_grade = self.diem_anh + self.diem_toan + self.diem_van
        aver = sum_grade / 3

        if aver >= 8:
            print('Gioi')
        elif aver < 8 and aver >= 6:
            print('Kha')
        else:
            print('Trung binh')


student01 = Student('Tuan Anh', 6, 3, 10)
student02 = Student('Peter Tran', 8, 9, 10)

print(student01.getAverGrade())
print(student02.getAverGrade())

student01.getAbility()
student02.getAbility()
