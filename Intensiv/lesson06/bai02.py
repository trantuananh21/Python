def UCLN(x, n):
    if n == 0:
        return x
    else:
        return UCLN(n, x%n)
    
print(UCLN(10,12))
# Output: 2
print(UCLN(3,6))
# Output: 3
