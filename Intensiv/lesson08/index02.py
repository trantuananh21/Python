b = [1,34,20,14,4]

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

print(sel_sort(b))

def bin_search(arr):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] % 2 == 0:
            return mid
    return -1

print('Vi tri so chan ban can tim la', bin_search(b))