# 1
num = [5, 1, 8, 92, -1, 30]

checkNum = int(input('Input a number: '))

if checkNum in num:
    position = num.index(checkNum)
    print('Number found at position', position)
else:
    print('Number not found')


# 2
num = [5, 1, 8, 92, -1, 30]
total=0
i=0
while (i < len(num)):
    total=total+num[i]
    i=i+1

print('Sum of numbers in list:', total)

# 3
print('''
Input the list of numbers. 
Enter 0 to finish.
''')
      
numList = []
while True:
    value = int(input(''))
    if value != 0:
        numList.append(value)
    else: break
sum_of = sum(numList)

print('Sum of numbers in list:', sum_of)