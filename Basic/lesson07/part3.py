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

# Bài 3 em làm khác một chút, thay vì dùng số 0 để dừng thì em viết tất cả các chữ số rồi ấn enter là xong
# 3
inputNumber = input('''
Viết cách chữ số với 
một điều kiện cách các 
chữ số bằng dấu cách: 
''')
list  = inputNumber.split()
sum = 0
for num in list:
    sum += int (num)
print("Sum = ",sum)
