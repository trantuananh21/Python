# Bài 1
# arr = [0,1,2,3,4,5,6,7,8,9]

# addTwoList = list()
# mulTwoList = list()

# for i in arr:
#     addTwo = i + 2
#     addTwoList.append(addTwo)
#     mulTwo = i * 2
#     mulTwoList.append(mulTwo)

# shiftTwoList = arr[2:] + arr[:2]

# print('Original array: ', arr)
# print('Add 2: ', addTwoList)
# print('Multipy 2: ', mulTwoList)
# print('Shift 2: ', shiftTwoList)


# Bài 2
# arr2 = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l',
#         'o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']

# arr2.reverse()
# print(arr2)

# Bài 3
# num = int(input('Input a positive number: '))

# num1, num2 = 1, 1
# count = 0

# if num <= 0:
#     print('It must bigger than 0')
# elif num == 1:
#     print('First 1 Fibonacci number(s): 1')
# elif num > 1:
#     print(f'First {num} Fibonacci number(s):')
#     while count < num:
#        print(num1, end=' ')
#        nth = num1 + num2
#        num1 = num2
#        num2 = nth
#        count += 1

# Bài 4
# menu = (('Ribeye Steak', 30.5), ('Potato Salad', 5), ('Sparkling Wine', 7), 
#         ('Smoked Salmon', 12), ('Chicken Soup', 12.5), ('Tiramisu Cake', 4.5))
# print(menu[0])


# Bài 5
# inputStr = input('Write a sentence: ')
# wordList = inputStr.split(' ')
# length = len(wordList)
# print('Number of unique words:', length)