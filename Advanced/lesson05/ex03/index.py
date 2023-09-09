import math

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

if a == 0 and b == 0 and c == 0:
    print('Vo nghiem')
else:
    rect = b**2 - (4*a*c)
    
    if rect < 0:
        print('Vo nghiem')

    elif rect == 0:
        only_result = -b / (2*a)
        print(only_result)
    
    elif rect > 0:
        first_result = (-b + math.sqrt(rect)) / (2*a)
        second_result = (-b - math.sqrt(rect)) / (2*a)
        print(first_result)
        print(second_result)