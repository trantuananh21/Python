s=[1]*811
s[0],s[1]=0,0
for i in range(2,int(811**0.5)+1):
    for j in range(i*i,811,i):
        s[j]=0

def sodep(n):
    if n == 1:
        return 11
    j,i = 1,11
    while j < n:
        i += 1
        a,b = str(i),0
        for x in range(len(a)):
            b += (int(a[x]))**2
        if s[b]==1:
            j += 1
            kq = i
    return kq

print(sodep(2))