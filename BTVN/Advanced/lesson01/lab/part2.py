class circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14
    
class rectangle:
    def __init__(self, h, w) -> None:
        self.h = h
        self.w = w
    
    def perimeter(self):
        return (self.h + self.w) * 2
    
    def area(self):
        return self.h * self.w

shape = input('Shape (rectangle | circle): ')

if shape == 'circle':
    radius = float(input('Radius: '))

    newCircle = circle(radius)
    print('=> Perimeter:', newCircle.perimeter())
    print('=> Area:', newCircle.area())

elif shape == 'rectangle':
    height = float(input('Height: '))
    width = float(input('Width: '))

    newRect = rectangle(height, width)
    print('=> Perimeter:', newRect.perimeter())
    print('=> Area:', newRect.area())

else:
    print('Invalid')