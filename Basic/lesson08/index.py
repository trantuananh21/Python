#-------------- Function, Scope, Modules ------------

# Nhan 2
# def mul2(n):
#     return n * 2

# a2 = mul2(1)
# b2 = mul2(2)
# c2 = mul2(3)

# print(a2, b2, c2)

# # Nhan 3
# def mul3(n):
#     return n * 3

# a3 = mul3(1)
# b3 = mul3(2)
# c3 = mul3(3)

# print(a3, b3, c3)

# def func():
#     print('Hello')
# func()

# def myName():
#     name = input('Your name is: ')
#     print('Hello', name)
# myName()

# parameters a,b,c: tham so
# arguments 3,4,8: doi so
# def sum(a: float,b: float,c: float):
#     s = a + b + c
#     return s
# k = sum(3,4.5,8)
# print(k)


# def greeting(name, lang):
#     if lang == 'vi':
#         print(f'Xin chao {name}')
#     elif lang == 'de':
#         print(f'Hallo {name}')
#     elif lang == 'en':
#         print(f'Hello {name}')
#     else:
#         print('Your langue is not supported')
# # positional arguments
# greeting('Tuan', 'de')
# # keyword arguments
# greeting(lang= 'vi', name = 'Tuan')

# def max(a, b, c):
#     if a >= b and a>=c:
#         return a
#     elif b >= a and b >=c:
#         return b
#     elif c >= b and c >=b:
#         return c
    
# inputs = [3,4,6]
# # Unpacking
# # print(max(inputs)) error
# print(max(*inputs))

# def max(*args):
#     res = args[0]
#     for arg in args[1:]:
#         if arg > res:
#             res = arg
#     return res
# print(max(1,34,3,6,7,9))


# name = 'MindX'  # global
# def greeting():
#     global name
#     # name = 'MindX Technology School'    #local
#     print(f'Hello {name}')
# print(f'Hi {name}')
# greeting()

# # local -> global
# def attack():
#     global hp 
#     hp = 0
# print(hp)



# Excersises
# 1
# def sum(*args):
#     total = 0
#     for arg in args[0:]:
#         total = total + arg
#     print(total)
# sum(1,5,1,6,3,4,90)

# 2
# def primeNum(*args):
#     for arg in args[0:]:
#         if arg == 1:
#             print('1 is not prime number')
#         elif arg > 1:
#             for i in range(2,arg):
#                 if (arg % i) == 0:
#                            print(arg,"is not a prime number")
#                            print(i,"times",arg//i,"is",arg)
#                            break
#                 else:
#                     print(arg,"is a prime number")
# primeNum(3,20,9,1)

# 3
def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('sir')) 