# 1
nameOfDist = ['BD', 'BTL', 'CG', 'DD', 'HBT']
popOfDist = [247100, 333300, 266800, 420900, 318000]

# 2
max = popOfDist[0]
for x in popOfDist:
    if x > max:
        max = x

min = popOfDist[0]
for y in popOfDist:
    if y < min:
        min = y

        
print(f'''
Most populated dist.: {popOfDist.index(max)}
Least populated dist.: {popOfDist.index(min)}
''')

# 3
print(f'''
Name of:
Most populated dist.: {nameOfDist[int(popOfDist.index(max)):int(popOfDist.index(max))+1]}
Least populated dist.: {nameOfDist[int(popOfDist.index(min)):int(popOfDist.index(min))+1]}
''')
