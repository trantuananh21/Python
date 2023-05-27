# 1
myList = [5, 1, 8, 92, 7, 30]
evenList = []

for i in myList:
    if i % 2==0:
        evenList.append(i)
        
print('Even numbers: ', evenList)

# 2
total = 0
input = input('''
Input the list of numbers.
Enter 0 to finish.

''')

while input != 0:
    for i in range(0, int(input)):
        total = total + int(i)
        i = i+i
    if input == 0:
        print('Sum of numbers in list:', total)