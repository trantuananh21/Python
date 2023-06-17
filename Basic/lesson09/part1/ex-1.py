# 1
num = int(input('Input a number: '))
def is_prime(n):
    if n % 2 == 0:
        return True
        
if is_prime(num):
    print('This number is even') 
else:
    print('This number is not even')