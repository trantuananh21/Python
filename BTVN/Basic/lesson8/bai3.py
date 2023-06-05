def is_prime(n):  
    for i in range(2,n//2+1):  
        if(n%i==0):  
            return(0)  
    return(1)
  
num =int(input("Enter a number: "))  
i=2
lst=[]
while(1):  
    if is_prime(i):  
        lst.append(i) 
        if len(lst)==num: 
            break 
    i+=1 
print(f'First {num} prime(s):',end=" ") 
print(*lst)