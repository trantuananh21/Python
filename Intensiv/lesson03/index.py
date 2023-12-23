# De Quy

# Giai thua
# def giai_thua(n):
#     if n <= 1:
#         return 1
#     else:
#         return n*giai_thua(n-1)
    
# print('5! =', giai_thua(5))
# print('4! =', giai_thua(4))
# print('3! =', giai_thua(3))
# print('2! =', giai_thua(2))
# print('1! =', giai_thua(1))


# Luy thua
# def luy_thua(x,n):
#     if n == 0:
#         return 1
#     else:
#         return x * luy_thua(x, n-1)
    
# print('3^2 =', luy_thua(3,2))
# print('9^0 =', luy_thua(9,0))


# Sum of Fibonacci
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))

# nterms = 5
# sum_of = 0
# if nterms <= 0:
#    print("Khong thoa man")
# else:
#    for i in range(nterms):
#        sum_of += recur_fibo(i)

# print(f'Tong cua day so Fibonacci den {nterms} la {sum_of}')


# Uoc chung lon nhat
# def ucln(x,n):
#     if n == 0:
#         return x
#     return ucln(n, x % n)

# print('Uoc so chung lon nhat cua x va n la: ', ucln(30, 48))

# In day so
# def day_so(n):
#     if n <= 0:
#         return 0
#     else:
#         day_so(n-1)
#         print(n)
    
# day_so(5)

# Fibonacci
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))

# nterms = 5

# if nterms <= 0:
#    print("Khong thoa man")
# else:
#    print("Day Fibonacci:")
#    for i in range(nterms):
#        print(recur_fibo(i))


# Tong uoc cua so nguyen duong
def tong_uoc(n, i):
    if i > n // 2:
        return 1
    elif i < n // 2:
        return i + tong_uoc(n, i-1)
    else:
        print(n)

print(tong_uoc(6))

# n = 6
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)