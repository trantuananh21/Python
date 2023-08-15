class Square:
    def __init__(self, len) -> None:
        self.len = len

    def cal_area(self):
        return self.len**2
    

class Cube(Square):
    def __init__(self, len) -> None:
        self.len = len

    def cal_area(self):
        return self.len**2 * 6
    
    def cal_volume(self):
        return self.len**3
    
square = Square(2)
print('Square area:', square.cal_area())

cube = Cube(2)
print('Cube area:', cube.cal_area())
print('Cube volume:', cube.cal_volume())