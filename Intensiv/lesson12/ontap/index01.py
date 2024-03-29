# # Merge Sort
# def mergeSort(arr):
# 	if len(arr) > 1:

# 		mid = len(arr)//2

# 		L = arr[:mid]

# 		R = arr[mid:]

# 		mergeSort(L)

# 		mergeSort(R)

# 		i = j = k = 0

# 		while i < len(L) and j < len(R):
# 			if L[i] <= R[j]:
# 				arr[k] = L[i]
# 				i += 1
# 			else:
# 				arr[k] = R[j]
# 				j += 1
# 			k += 1

# 		while i < len(L):
# 			arr[k] = L[i]
# 			i += 1
# 			k += 1

# 		while j < len(R):
# 			arr[k] = R[j]
# 			j += 1
# 			k += 1


# def printList(arr):
# 	for i in range(len(arr)):
# 		print(arr[i], end=" ")
# 	print()


# arr = [34, 11, 68, 5, 84]
# print("Given array is")
# printList(arr)

# mergeSort(arr)
# print("\nSorted array is ")
# printList(arr)


# Quick Sort
def QuickSort(arr):

    elements = len(arr)
    
    if elements < 2:
        return arr
    
    current_position = 0 #Position of the partitioning element

    for i in range(1, elements): #Partitioning loop
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp 
    
    left = QuickSort(arr[0:current_position]) 
    right = QuickSort(arr[current_position+1:elements])

    arr = left + [arr[current_position]] + right 
    
    return arr



array_to_be_sorted = [4,2,7,3,1,6]
print("Original Array: ",array_to_be_sorted)
print("Sorted Array: ",QuickSort(array_to_be_sorted))