import math
a = int(input('Input a: '))
b = int(input('Input b: '))
c = int(input('Input c: '))

if a <= 0:
    print('A must be bigger than 0')
else:
    my_num01 = b**2 - (4*a*c)
    my_num02 = math.sqrt(my_num01)

    final_num01 = (-b + my_num02) / (2*a)
    final_num02 = (-b - my_num02) / (2*a)

    print('The equation has 2 solutions.')
    print(f'x = {final_num01} or x = {final_num02}')