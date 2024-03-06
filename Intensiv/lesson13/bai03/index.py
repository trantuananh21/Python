a = [1, 4, 5, 12, 2, 45, 63, 102, 99, 87, 47, 65]
# Bubble Sort
# def bubble_sort(arr):
#     n = len(arr) # Độ dài của mảng

#     for i in range(n): # Vòng lặp for i chạy từ 0 đến n - 1
#         for j in range(0, n-i-1): # Vòng lặp for j trong vòng lặp for j chạy từ 0 đến đến n - i - 1
#             if arr[j] > arr[j+1]: # Nếu có nghịch số của hai số liền kề thì đổi chỗ hai số cho nhau
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp
    
#     return arr

# print(bubble_sort(a))

# Selction Sort
# def selection_sort(arr):
#     n = len(arr)

#     for i in range(n-1):
#         min = i # So nho nhat ban dau la so dau tien trong day

#         for j in range(i, n): # Những số xếp đầu tiên sẽ không phải duyệt vì nó đã được sắp xếp rồi
#             if arr[min] > arr[j]: # Tìm min cho dãy chưa được sắp xếp
#                 min = j

#         if min != i: # Nếu có nghịch số thì số nhỏ nhất của dãy chưa được sắp xếp sẽ lên đầu
#             temp = arr[i]
#             arr[i] = arr[min]
#             arr[min] = temp

#     return arr

# print(selection_sort(a))

# def QuickSort(arr):

#     n = len(arr) # Độ dài của mảng
    
#     current_position = 0 # Vị trí chọn

#     for i in range(1, n):
#          if arr[i] <= arr[0]: # Nếu số đầu tiên của mảng lớn hơn hoặc bằng số i thì:
#               current_position += 1 # Vị trí chọn tăng thêm 1 đơn vị

#               # Đổi số i với số của vị trí chọn
#               temp = arr[i]
#               arr[i] = arr[current_position]
#               arr[current_position] = temp

#     # Đổi vị trí số ban đầu với số của vị trí chọn
#     temp = arr[0]
#     arr[0] = arr[current_position] 
#     arr[current_position] = temp 
    
#     # Dãy số bên trái
#     left = QuickSort(arr[0:current_position]) 
#     # Dãy số bên phải
#     right = QuickSort(arr[current_position+1:n])

#     # Cả mảng sẽ bằng dãy số cộng số ở vị trí chọn cộng dãy bên phải
#     arr = left + [arr[current_position]] + right 
    
#     return arr

# print(QuickSort(a))