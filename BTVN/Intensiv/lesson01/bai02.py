class Book():
    def __init__(self, ten, tac_gia, nam_xuat_ban, so_trang):
        self.ten = ten
        self.tac_gia = tac_gia
        self.nam_xuat_ban = nam_xuat_ban
        self.so_trang = so_trang

    def getInfo(self):
        return self.ten, self.tac_gia, self.nam_xuat_ban, self.so_trang
    
    def checkNew(self):
        if self.nam_xuat_ban > 2020:
            return True
        else:
            return False
    
book01 = Book('Hello Python', 'Tuan', 2024, 303)
book02 = Book('Hello Javascript', 'Dat', 2019, 284)

print(book01.getInfo())
print(book02.checkNew())