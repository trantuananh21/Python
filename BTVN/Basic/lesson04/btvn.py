# Bài 1
star = int(input('Input number: '))
for i in range(star):
    for j in range(i+1):
       print("# ", end="")
    print("")


# Bài 2
num1 = float(input('Input a positive number: '))
while num1 < 0:
    num1 = float(input('Please input a positive number: '))

    if num1 > 0:
        print("Thank you.")


# Bài 3
num2 = int(input('Input number: '))
nhan = 1

if num2 >= 1:
    for i in range(1, num2+1):
        nhan = nhan * i
        print(num2,'! = ', nhan)

elif num2 == 0:
    print('0! = 1')

elif num2 < 0:
    print("Invalid")


# Bài 4
num3 = int(input('Input number: '))
total = 0

while num3 > 0:
    total = total + num3 % 10
    num3 = int(num3/10)

    print(total)


# Bài 5
count = 0

def sum(x):
    num4 = 0
    while x != 0:
        num4 += x %10
        x = int(x/10)
    return num4

print('Number with sum of digits = 9:')

for num4 in range (1000,10000):
    if sum(num4) == 9:
        count = count + 1
        print(num4, end=' ')
        if count == 10:
            break


# Bài 6 
num5 = int(input('Input number of edges: '))
angle = 360/num5

for i in range(num5):
    import turtle as t
    t.forward(100)
    t.left(angle)

t.mainloop()

# em không làm theo gợi ý của bài nhưng kết quả cho ra thì vẫn đúng ạ

# Bài 7
import turtle as t

for r in range(100):
    t.forward(2+r)
    t.right(30)

t.mainloop()