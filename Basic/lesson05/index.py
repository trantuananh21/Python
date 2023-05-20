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
print('Input a month: ', end='')
month = int(input())

if month == 1 or month == 3 or month == 5 or\
   month == 7 or month == 8 or month == 10 or month == 12:
  print('This month has 31 days')
elif month == 4 or month == 6 or month == 9 or month == 11:
  print('This month has 30 days')
elif month == 2:
  print('This month has 28 or 29 days')
else:
  print('Invalid month')

# Phần 4
# 1.
username = input('Username: ')
password = input('Password: ')
email = input('Email: ')

print('Registered successfully.')

# 2.
userName = input('Username: ')
passWord = input('Password: ')

while True:
  repeatPass = input('Repeat password: ')
  if repeatPass == passWord:
    break
  else:
    print('Passwords not match. Please input again.')

email1 = input('Email: ')
print('\nRegistered successfully.')

# 3.
Username = input('Username: ')

# Check đủ hơn 8 chữ số trong một mật khẩu
while True:

  print('\nPassword: ', end='')
  password1 = input()
  
  has_letter = False
  has_digits = False
  for ch in password1:
    if (ch > 'a' and ch < 'z') or (ch > 'A' and ch < 'Z'): 
      has_letter = True
    if ch > '0' and ch < '9':  
      has_digits = True
  
  if has_letter and has_digits and len(password1) >= 8:
    break
  else:
    print('Invalid password. Please input again.', end='')


# Check hai mật khẩu có trùng nhau không
while True:
  print('Repeat password: ', end='')
  if input() == password1:
    break
  else:
    print('Passwords not match. Please input again.')

# Check gmail có hợp lệ hay không
while True:

  print('\nEmail: ', end='')
  email = input()

  if ('.' in email) and ('@' in email):
    break
  else:
    print('Invalid email. Please input again.', end='')

print('\nRegistered successfully.')


# Phần 5
# print('''
# == FREAKING MATH CONSOLE ==
# Give correct answers to get scores.
# ''')
# import random
# import operator

# def randomProblem():
#     operators = {
#         '+' : operator.add,
#         '-': operator.sub,
#         '*': operator.mul,
#         '/': operator.truediv,
#     }

#     num10 = random.randint(1,30)
#     num11 = random.randint(1,20)
#     operation = random.choice(list(operators.keys()))
#     answer = operators.get(operation)(num10, num11)
#     print(f'What is {num10} {operation} {num11}?')
#     return answer

# def askQuestion():
#     answer = randomProblem()
#     guess = float(input())
#     return answer == guess

# def game():
#     score = 0
#     for i in range(5):
#         if askQuestion() == True:
#             score += 1
#             print('Correct, your recently score is:', score)
#         else:
#             print(f'''
#             Incorrect
#             Your score is {score}
#             == GAME OVER ==
#             ''')
#             break
#         if score == 5:
#             print(f'''
#             == YOU WIN ==
#             Your score is {score}
#             ''')
# game()

# Game 2
import random
import time

# GAME INTRO
print('\n== FREAKING MATH CONSOLE ==')
print('Give correct answers to get scores.\n')


# GAMEPLAY
score = 0  # user's score

while True:  # while playing
  
  # initialize operations in + - * /
  op = random.randint(0, 3)
  left = None     # left operand
  right = None    # righgt operand
  result = None   # operation result
  op_char = None  # operation character: + - * /
  second = 0

  # randomize operator & operands (toán tử và toán hạng)
  if op == 0:    # ADDITION +
    for i in range(5):
      left = random.randint(0, 20)
      right = random.randint(0, 20)
    for i in range(6,10):
      left = random.randint(10, 30)
      right = random.randint(10, 30)
    for i in range(10,20):
      left = random.randint(40, 60)
      right = random.randint(30, 40)
    result = left + right
    op_char = '+'
    time.sleep(second)
    if second == 5:
      print('== GAME OVER ==')
      print(f'Your total score is {score}')


  elif op == 1:  # SUBTRACTION -
    for i in range(5):
      left = random.randint(0, 20)
      right = random.randint(0, 20)
    for i in range(6,10):
      left = random.randint(10, 30)
      right = random.randint(10, 30)
    for i in range(10,20):
      left = random.randint(40, 60)
      right = random.randint(30, 40)
    result = left - right
    op_char = '-'
    time.sleep(second)
    if second == 5:
      print('== GAME OVER ==')
      print(f'Your total score is {score}')


    
  elif op == 2:  # MULTIPLICATION *
    for i in range(5):
      left = random.randint(0, 10)
      right = random.randint(0, 10)
    for i in range(5,10):
      left = random.randint(10, 20)
      right = random.randint(10, 20)
    for i in range(10,20):
      left = random.randint(20, 30)
      right = random.randint(20, 30)
    result = left * right
    op_char = '*'
    time.sleep(second)
    if second == 5:
      print('== GAME OVER ==')
      print(f'Your total score is {score}')


  elif op == 3:  # DIVISION /
    for i in range(5):
      left = random.randint(0, 10)
      right = random.randint(0, 10)
    for i in range(5,10):
      left = random.randint(20, 30)
      right = random.randint(10, 20)
    for i in range(10,20):
      left = random.randint(40, 60)
      right = random.randint(30, 40)
    result = left / right  # make sure result is whole number
    op_char = '/'
    time.sleep(second)
    if second == 5:
      print('== GAME OVER ==')
      print(f'Your total score is {score}')


  # randomize if this expression is correct
  correct_ans = random.randint(0, 1)  # 1 for correct, 0 for incorrect
  if not correct_ans:  # if incorrect, add to result a random number in [-5, -1] and [1, 5]
    result += (random.randint(0, 1)*2-1) * random.randint(1, 5)
  
  # print the expression & get user input
  print(f'{left} {op_char} {right} = {result}')
  print('1 for True, 0 for False: ', end='')
  choice = input()
  if str(correct_ans) == choice:  # if correct answer, increase score & continue game
    score += 1
    print(f'Score: {score}\n')
  else:                           # if incorrect, end the game
    print(f'Incorrect.\n')
    break

# annouce game result
print('== GAME OVER ==')
print(f'Your total score is {score}')