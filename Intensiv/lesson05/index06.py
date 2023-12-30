def search(arr, n):
    for i in arr:
        for j in arr:
            if i + j == n:
                return(i,j)
            
    return -1

l = [1, 3, 8, 9, 10, 15, 41, 59, 64, 100]
print(l)

x = int(input('Nhap so cua ban: '))
print(search(l, x))