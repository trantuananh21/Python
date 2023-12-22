class Sach():
    def __init__(self):
        self.ma = input('Ma sach: ')
        self.ten = input('Ten sach: ')
        self.nha_xuat_ban = input('Nha xuat ban: ')
        self.so_trang = int(input('So trang: '))
        self.gia = float(input('Gia tien: '))

    def display(self):
        print(f'''
Ma: {self.ma}
Ten hang: {self.ten}
Nha xuat ban: {self.nha_xuat_ban}
So trang: {self.so_trang}
Gia: {self.gia}
'''
        )

sach01 = Sach()

sach01.display()