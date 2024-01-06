a=[1,2,5,7,15,22,41,55,65,73,82,91]

# Tim kiem tuyen tinh
x = 73
index = 0

for i in a:
    index += 1
    if x == i:
        print(index-1)
if index == 0:
    print('So cua ban khong co trong list')
# Output: 9


# def search(arr, n):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left+right) // 2

#         if arr[mid] == n:
#             return mid
        
#         elif arr[mid] < n:
#             left = mid + 1

#         else:
#             right = mid - 1

#     return -1

# print(search(a,73))
# Output: 9