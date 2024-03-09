# Day so mac dinh
a = [4, 2, 38, 42, 59, 7]
print(a)

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    
    return arr

print('Sau khi sort:', bubble_sort(a))

# Tim vi tri so
def bin_search(arr, n):
    left = 0
    right = len(arr)

    while left <= right:
        mid = (left+right) // 2

        if arr[mid] == n:
            return mid
        if arr[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

print(bin_search(a,7))

# Xoa thanh phan nho nhat
def delete_min(arr):
    min = arr[0]
    n = len(arr)

    for i in range(n):
        if arr[i] < min:
            min = arr[i]
    
    arr.remove(min)
    return arr

print('Sau khi xoa thanh phan nho nhat', delete_min(a))

# Add them phan tu
x = 98
k = 2
a.insert(k, x)
print(a)