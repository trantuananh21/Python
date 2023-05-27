# 1
nameOfDist = ['BD', 'BTL', 'CG', 'DD', 'HBT']
popOfDist = [247100, 333300, 266800, 420900, 318000]
area = [9.224, 43.35, 12.04, 9.96, 10.09]

listZip = zip(nameOfDist, popOfDist, area)
zippedList = list(listZip)

for i in zippedList:
    print(f'''{i[0]}: {i[1]/i[2]}''')

# 2
sumOfDist = 0
sumOfPop = sum(popOfDist)
listDensity = []
for i in zippedList:
    sumOfDist += 1
    mat = i[1]/i[2]
    listDensity.append(mat)

sumOfDensity = sum(listDensity)
avg = sumOfDensity / sumOfDist
print('Average population density:', avg)

