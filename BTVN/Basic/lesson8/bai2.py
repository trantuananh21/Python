num = int(input('Input a number: '))
def is_prime(n):
    if n < 1:
        return False
    for i in range(2, 1+n//2):
        if (n % i) == 0:
            return False
    
    else:
        return True
        
if is_prime(num):
    print(f'{int(num)} is a prime') 
else:
    print(f'{num} is not a prime')