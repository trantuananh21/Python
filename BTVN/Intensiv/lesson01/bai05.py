class Contact():
    def __init__(self, ten, sdt, email):
        self.ten = ten
        self.sdt = sdt
        self.email = email

    def getInfo(self):
        return self.ten, self.sdt, self.email

person01 = Contact('Tuan Anh', '09201830', 'tuanvananh@gmail.com')
person02 = Contact('Bang Anh', '093821231', 'bangthianh@gmail.com')

print(person01.getInfo())
print(person02.getInfo())