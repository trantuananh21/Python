# Bai 1
height = float(input('Chieu dai: '))
weight = float(input('Chieu rong: '))

def perimeter(x, y):
    return (x + y) * 2

def area(x, y):
    return x * y

print('Chu vi hinh chu nhat la:', perimeter(height, weight))
print('Dien tich hinh chu nhat la:', area(height, weight))