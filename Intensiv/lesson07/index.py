# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp
    
#     return arr

# a = [0,9,1,5]
# b = bubble_sort(a)
# print(b)

# def bin_search(arr, n):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == n:
#             return mid
#         elif arr[mid] < n:
#             left = mid + 1
#         else:
#             right = mid -1

#     return -1

# print(bin_search(b, 9))

# a = [0,9,1,5]
# x = 9
# index = -1

# for i in a:
#     index += 1
#     if i == x:
#         print(index)
# if index == -1:
#     print('-1')

# Selection Sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min = i
        
        for j in range(i, n):
            if arr[j] < arr[min]:
                min = j

        if min != i:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp

    return arr

b = [7,5,8,4]
print(selection_sort(b))