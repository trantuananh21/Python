num = input('Input number: ')

def is_int(n):
    if n.isnumeric():
        return True
    else:
        return False
    
if is_int(num):
    print(f'{int(num)} is an integer')
else:
    print(f'{num} is not an integer')