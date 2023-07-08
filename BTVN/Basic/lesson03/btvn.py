# Bài 1
num1 = int(input("Input number: "))

if num1 % 2 == 0:
    print(num1, 'is even')
else:
    print(num1, 'is odd')
# //////////////////////////////


# Bài 2
intNum = float(input("Input number: "))

if intNum//1 ==  intNum:
    print(intNum, "is an integer")
else:
    print(intNum, "is not an integer")
# //////////////////////////////


# Bài 3
num2 = input('Input character: ')

if num2.isdigit():
    print(num2, "is a digit")
else:
    print(num2, "is not a digit")
# //////////////////////////////


# Bài 4
num3 = int(input('Input number: '))

if num3 % 3 == 0 and num3 % 5 == 0:
    print(num3, 'is divisible by 3 and 5')

elif num3 % 3 == 0 and num3 % 5 != 0:
    print(num2, 'is divisible by 3 ')

elif num3 % 5 == 0 and num3 % 3 != 0:
    print(num2, 'is divisible by 5')

elif num3 % 5 != 0 and num3 % 3 != 0:
    print(num2, 'is not divisible by 3 or 5')
# //////////////////////////////


# Bài 5
print('Welcome to The Ultimate Sercurity System')
username = input('Username: ')
password = input('Password: ')

if username == 'admin' and password == '12345':
    print('You are logged in,', username)
else:
    print("Wrong username or password")
# //////////////////////////////



# Bài 6
len1 = int(input('Input length 1: '))
len2 = int(input('Input length 2: '))
len3 = int(input('Input length 3: '))

if (len1 + len2 > len3 
    and len2 + len3 > len1 
    and len1 + len3 > len2
    and len1 > 0 
    and len2 > 0 
    and len3 > 0 ):
    print('The 3 line segments can form a triangle.')
else:
    print('The 3 line segments cannot form a triangle.')
# //////////////////////////////


# Bài 7
len1 = int(input('Input length 1: '))
len2 = int(input('Input length 2: '))
len3 = int(input('Input length 3: '))

if len1 + len2 > len3 and len2 + len3 > len1 and len1 + len3 > len2:
    if len1 == len2 == len3:
        print('The 3 line segments can form an equilateral triangle.')
        import turtle as t
        t.forward(len1)
        t.left(120)
        t.forward(len2)
        t.left(120)
        t.forward(len3)
        t.mainloop()
        
    elif len1**2 + len2**2 == len3**2:
        print('The 3 line segments can form a right triangle.')
    else:
        print("The 3 line segments can form an triangle.")

else:
    print('The 3 line segments cannot form a triangle.')
#//////////////////////////////