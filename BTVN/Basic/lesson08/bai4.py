def sumOfFact(n):
    fact = 1
    sum  = 0
    if (n == 0 or n == 1):
        return fact
    else:
        for i in range(1, n + 1):
            fact = fact * i
            frac = fact / i
            sum = sum + frac
        return sum
 
n = int(input("Input a number: "))
print("Result: ", sumOfFact(n))