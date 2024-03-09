# Bubble Sort

# c = [2,19,15,14,4]

# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] < arr[j+1]:
#                 temp = arr[j] 
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp

#     return arr

# print(bubble_sort(c))

# Selection sort
# def selection_sort(arr):
#     n = len(arr)

#     for i in range(n-1):
#         min = i
        
#         for j in range(i, n):
#             if arr[j] < arr[min]:
#                 min = j

#         if min != i:
#             temp = arr[i]
#             arr[i] = arr[min]
#             arr[min] = temp

#     return arr

# b = [7,5,8,4]
# print(selection_sort(b))

# Insertion Sort
# a = [7,2,19,241,312]

# def insertion_sort(arr):
#     n = len(arr)

#     for i in range(1, n):
#         x = arr[i]
#         j = i -1

#         while j >= 0 and x < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#             arr[j+1] = x

#     return arr

# print(insertion_sort(a))

# Quick Sort
# def QuickSort(arr):

#     elements = len(arr)
    
#     if elements < 2:
#         return arr
    
#     current_position = 0

#     for i in range(1, elements):
#          if arr[i] <= arr[0]:
#               current_position += 1
#               temp = arr[i]
#               arr[i] = arr[current_position]
#               arr[current_position] = temp

#     temp = arr[0]
#     arr[0] = arr[current_position] 
#     arr[current_position] = temp 
    
#     left = QuickSort(arr[0:current_position]) 
#     right = QuickSort(arr[current_position+1:elements])

#     arr = left + [arr[current_position]] + right 
    
#     return arr

# array_to_be_sorted = [4,2,7,3,1,6]
# print("Original Array: ",array_to_be_sorted)
# print("Sorted Array: ",QuickSort(array_to_be_sorted))

# Merge Sort
# def mergeSort(arr):
# 	if len(arr) > 1:

# 		mid = len(arr)//2

# 		left = arr[:mid]

# 		right = arr[mid:]

# 		mergeSort(left)

# 		mergeSort(right)

# 		i = j = k = 0

# 		while i < len(left) and j < len(right):
# 			if left[i] <= right[j]:
# 				arr[k] = left[i]
# 				i += 1
# 			else:
# 				arr[k] = right[j]
# 				j += 1
# 			k += 1

# 		while i < len(left):
# 			arr[k] = left[i]
# 			i += 1
# 			k += 1

# 		while j < len(right):
# 			arr[k] = right[j]
# 			j += 1
# 			k += 1
			
# 		return arr

# arr = [34, 11, 68, 5, 84]
# print("Given array is", arr)
# print("\nSorted array is ", mergeSort(arr))