class BankAccount():
    def __init__(self,stk, ten, so_du):
        self.stk = stk
        self.ten = ten
        self.so_du = so_du

    def getInfo(self):
        return self.stk, self.ten, self.so_du

    def napTien(self):
        so_tien_chuyen = float(input('So tien ban muon chuyen: '))
        self.so_du = so_tien_chuyen + self.so_du
        return self.so_du
    
    def rutTien(self):
        so_tien_rut = float(input('So tien ban muon rut: '))
        if so_tien_rut < self.so_du:
            self.so_du = self.so_du - so_tien_rut
            return self.so_du
        else:
            return False

    
bank01 = BankAccount(1234512, 'Tran Tuan Anh', 340000)
bank02 = BankAccount(5432154, 'Peter Maximanh', 5000000)

print(bank01.napTien())
print(bank02.rutTien())
print(bank01.getInfo())
print(bank02.getInfo())
