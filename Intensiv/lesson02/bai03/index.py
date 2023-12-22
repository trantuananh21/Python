class HangHoa():
    def __init__(self):
        self.ma = input('Ma hang: ')
        self.ten = input('Ten hang: ')
        self.gia = float(input('Gia: '))
        self.so_luong = int(input('So luong: '))

    def display(self):
        print(f'''
Ma: {self.ma}
Ten hang: {self.ten}
Gia: {self.gia}
So luong: {self.so_luong}
'''
        )

hang01 = HangHoa()

hang01.display()