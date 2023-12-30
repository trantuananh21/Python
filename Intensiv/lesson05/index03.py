# Tim kiem tuyen tinh
# l = [1, 3, 8, 9, 10, 15, 41, 59, 64, 100]
# print(l)

# x = 10
# k = -1
# index = 0

# for i in l:
#     index += 1
#     if i == x:
#         k = i
#         print('So ban can tim nam o vi tri', index-1)
    
# if k == -1:
#     print('So cua ban khong co trong list')

def search(arr, n):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left+right) // 2

        if arr[mid] == n:
            return mid
        
        elif arr[mid] < n:
            left = mid + 1

        else:
            right = mid - 1

    return -1

l = [1, 3, 8, 9, 10, 15, 41, 59, 64, 100]
print(l)
x = 10

print('So ban can tim nam o vi tri', search(l, x))