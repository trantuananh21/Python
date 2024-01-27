a = [4, 12, 5, 8, 70, 6]

# Số nhỏ nhất
def min(arr):
    min = arr[0]

    for i in arr:
        if i < min:
            min = i

    return min

# Sắp xếp tăng dần
def sel_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min = i

        for j in range(i,n):
            if arr[j] < arr[min]:
                min = j

        if min != i:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp

    return arr

# Số lớn nhất
def max(arr):
    max = arr[0]

    for i in arr:
        if i > max:
            max = i

    return max

print('So nho nhat:', min(a))
print('Sap xep:', sel_sort(a))
print('So lon nhat:', max(a))

# Tìm số k
k = 3
n = len(a)

for i in range(n):
    if k <= n:
        if i == k:
            print('So k:', a[i])

if k > n:
    print('k khong thoa man')

# Chèn thêm phần tử 66 vào vị trí thứ 4
a.insert(4, 66)
print('Sau khi chen 66 vao vi tri thu 4')
print(a)