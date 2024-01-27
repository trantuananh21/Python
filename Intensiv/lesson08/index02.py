b = [3,34,20,14,4]

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

def bin_search(arr):
    sel_sort(b)

    for i in arr:
        smallest = arr[0]
        if i % 2 == 0 and i < smallest:
            i = smallest

    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < smallest:
            left = mid + 1
        elif arr[mid] > smallest:
            right = mid - 1
        else:
            return mid
    return -1

print(sel_sort(b))
print('Vi tri so chan ban can tim la', bin_search(b))