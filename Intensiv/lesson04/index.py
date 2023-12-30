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

# Tìm kiếm tuyến tính: duyệt tất cả toàn bộ phần tử có trong mảng để tìm ra phân tử cần tìm
# Tìm kiếm nhị phân: nó chỉ dùng được khi list đã được sắp xếp, có thể tăng dần hoặc giảm dần