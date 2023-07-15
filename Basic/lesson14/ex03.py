def isPalindrome(x):
	return x == x[::-1]

my_txt = input('Input a text: ')
ans = isPalindrome(my_txt)

if ans:
	print("Yes")
else:
	print("No")
