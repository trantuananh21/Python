import turtle as t

class HinhChuNhat():
    def __init__(self) -> None:
        self.chieu_dai = float(input('Chieu dai: '))
        self.chieu_rong = float(input('Chieu rong: '))

    def draw(self):
        for _ in range(4):
            t.forward(self.chieu_dai)
            t.right(90)
            t.forward(self.chieu_rong)

        t.done()

    def perimeter(self):
        return (self.chieu_dai + self.chieu_rong)*2
    
    def area(self):
        return self.chieu_dai * self.chieu_rong


rect01 = HinhChuNhat()

rect01.draw()
print('Chu vi:', rect01.perimeter())
print('Dien tich:', rect01.area())