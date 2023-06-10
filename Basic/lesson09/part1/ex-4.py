mytxt = input('Input a text: ')

def is_palindrome(x):
    rev = ''.join(reversed(x))

    if (x == rev):
        return True
    return False

ans = is_palindrome(mytxt)

if ans:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")