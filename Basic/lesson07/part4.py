# 1
myList = [5, 1, 8, 92, 7, 30]
evenList = []

for i in myList:
    if i % 2==0:
        evenList.append(i)
        
print('Even numbers: ', evenList)

# 2
print('''
Input the list of numbers. 
Enter 0 to finish.
''')
      
evenList = []
while True:
    value = int(input(''))
    if value != 0:
        if value % 2 == 0:
            evenList.append(value)
    else: break
print('Even numbers in list:', evenList)