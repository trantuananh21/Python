def search(arr, n):
    for i in arr:
        if i > n:
            if i - n == 2:
                return i
        else:
            if n - i == 2:
                return i
            
    return -1
    
l = [1, 3, 8, 9, 10, 15, 41, 59, 64, 100]
print(l)

x = int(input('Nhap so cua ban: '))
print(search(l, x))