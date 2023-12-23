a = []
n = int(input('So phan tu co trong mang: '))

for i in range(n):
    num = int(input(f'Nhap so [{i}]: '))
    i+1
    a.append(num)

print(a)

x = int(input('Nhap so ban muon tim: '))
k = -1
index = 0
for i in a:
    index = index + 1
    if i == x:
        k = i
        print('So ban muon tim nam o vi tri', index-1)
if k == -1:
    print('Khong tim duoc so do trong list')