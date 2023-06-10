def frac(n):
    fraction = 1
    if (n == 0 or n == 1):
        return fraction
    else:
        for i in range(2, n + 1):
            fraction = fraction * i
        return fraction

num = int(input('Input a number: '))

myNum = frac(num)

print(f'{num}! = {myNum}')