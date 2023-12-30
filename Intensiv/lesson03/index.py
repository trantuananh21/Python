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
l = []
def factors(n, i):
    if (i <= n):
        if (n % i == 0):
            l.append(i)
         
        factors(n, i + 1)

factors(9,1)
print(l)
print(sum(l))

# i là số đếm từ 1 đến số n, khi số i nhỏ hơn hoặc bằng n thì sẽ có 
# dòng kiểm tra n chia số đó có dư bằng không hay không, nếu đúng thì append làm list l
# sau đó trả về factors(n,i+1) để i tăng thêm một số
# vd: n = 3 và i = 1
# vì i = 1 nhỏ hơn 3 nên chạy dòng kiểm tra 3 chia 1 có dư bằng 0 không
# vì 3 chia hết cho 1 nên số một sẽ được thêm vào list l
# sau đó function trả về factors(3, 1+1) => n = 3 và i = 2
# function sẽ chạy đến khi i = n, khi i = n thì function sẽ ngừng chạy
