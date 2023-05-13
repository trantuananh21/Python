# Phần 1
# 1.
firstName = input('Your First name: ')
lastName = input('Your Last name: ')
fullName = firstName + ' ' + lastName

print('Your full name is:', fullName)

# 2.
yourInput = input('Your Input: ')

print('Capitalized:', yourInput.upper())


# 3.
num1 = float(input('Input your number: '))
square = num1**2

print('Squared input:', square)


# 4.
r = int(input("Input circle's radius: "))

import turtle as t
t.circle(r)
t.mainloop()


# Phần 2
# 1.
for i in range(3,13):
    print(i, end=' ')

# 2.
num2 = int(input('Input your number: '))

for i in range(0,num2+1):
    print(i, end=' ')

# 3.
num3 = int(input('Input a number: '))

for i in range(0, num3+1):
    if i % 2 != 0:
        print(i, end=' ')        


# 4.
num4 = int(input('Input your number: '))
angle = 360/num4

for i in range(num4):
    import turtle as t
    t.forward(100)
    t.left(angle)

t.mainloop()


# Phần 3
# 1.
num5 = int(input('Input a number: '))

if num5 > 13:
    print('This number is larger than 13')
else:
    print('This number is not larger than 13')

# 2.
num6 = int(input('Input a number: '))

if num6 % 2 == 0:
    print('This number is even')
elif num6 % 2 != 0:
    print('This number is not even')

# 3.
from calendar import monthrange
num7 = int(input('Input a month: '))

num_days = monthrange(2023, num7)[1]
print('This month has',num_days,'days')


# Phần 4
# 1.
username = input('Username: ')
password = input('Password: ')
email = input('Email: ')

print('Registered successfully.')

# 2.
userName = input('Username: ')
passWord = input('Password: ')
repeatPass = input('Repeat password: ')
email1 = input('Email: ')

while repeatPass != passWord:
    print('Passwords not match. Please input again.')
    repeatPass =  input('Repeat password: ')

# 3.
Username = input('Username: ')
password1 = input('Password: ')
repeatPass1 = input('Repeat password: ')
email2 = input('Email: ')

# # Check đủ hơn 8 chữ số trong một mật khẩu
alpha = 0
string= password1
for i in string:
    if (i.isalpha()):
        alpha+=1
if len(string)-alpha < 8:
    print('Invalid password')
    password1 = input('Repeat password: ')

# # Check hai mật khẩu có trùng nhau không
while repeatPass1 != password1:
    print('Passwords not match. Please input again.')
    repeatPass1 =  input('Repeat password: ')

# # Check gmail có hợp lệ hay không
at = '@gmail.com'

if at not in email2:
    print('Invalid email. Please input again')
    email2 = input('Email: ')

# Phần 5
print('''
== FREAKING MATH CONSOLE ==
Give correct answers to get scores.
''')
import random
import operator

def randomProblem():
    operators = {
        '+' : operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    num10 = random.randint(1,30)
    num11 = random.randint(1,20)
    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num10, num11)
    print(f'What is {num10} {operation} {num11}?')
    return answer

def askQuestion():
    answer = randomProblem()
    guess = float(input())
    return answer == guess

def game():
    score = 0
    for i in range(5):
        if askQuestion() == True:
            score += 1
            print('Correct, your recently score is:', score)
        else:
            print(f'''
            Incorrect
            Your score is {score}
            == GAME OVER ==
            ''')
            break
        if score == 5:
            print(f'''
            == YOU WIN ==
            Your score is {score}
            ''')
game()