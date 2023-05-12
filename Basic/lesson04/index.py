s = "Computer Science Basic"
for i in range(len(s)):
    if i %2 == 0:
        print(s[i], end=' ')

n = 1
while n < 100:
    print(n, end=' ')
    n = n*2
    print("After update:", n)



n = 1
for i in range(1_000):
    if 100 < i < 200:
        print(i, end = ' ')
    elif i >= 200: 
        print('Stop loop')
        break

    print("Running")




for i in range(10):
    if i% 2 != 0:
        continue
    print(i, end=' ')




n = int(input('Input number: '))
for i in range(1, 11):
   print(n, "x", i, '=', n*i)  

n = int(input('Input number: '))
total = 0
while n > 0:
    total = total + n %10
    n = int(n/10)
    print(total)

n = int(input('Input number: '))
for i in range(n, 0, -1):
    for j in range(0, i):
        print("* ", end="")
    print("")