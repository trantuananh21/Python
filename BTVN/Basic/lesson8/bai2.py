num = int(input('Input a number: '))
def primeNum(n):
    if n == 1:
        return False
    elif n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return False
            else: 
                return True
    else:
        return False
if primeNum(num):
    print(f'{int(num)} is a prime') 
else:
    print(f'{num} is not a prime')