def print_fibo(n):
   if n <= 1:
       return n
   else:
       return(print_fibo(n-1) + print_fibo(n-2))

num = int(input('Input a number: '))

# check if the number of terms is valid
if num <= 0:
   print("Plese enter a positive integer")
else:
   print(f'First {num} Fibonacci numbers:')
   for i in range(1, num+1):
       print(print_fibo(i))
