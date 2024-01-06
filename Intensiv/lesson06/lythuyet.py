# Thuật toán sắp xếp nổi bọt
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
a = [4,6,2,8]
print(bubble_sort(a))

# i = 0, n = 4, j in range(0, 4-0-1=3)
# arr[0]=4 < arr[0+1=1]=6 -> True
# Hoan doi: temp = 4 -> 4 = 6 -> 6 = temp
# a = [6,4,2,8]

# arr[1]=4 < arr[1+1]=2 -> False -> Khong hoan doi
# arr[2]=2 < arr[2+1]=8 -> True
# Hoan doi: temp = 2 -> 2 = 8 -> 8 = temp
# a = [6,4,8,2]

# i = 1, j in range(0,4-1-1=2)
# arr[0]=6 < arr[0+1]=4 -> False -> Khong hoan doi
# arr[1]=4 < arr[1+1]=8 -> True 
# Hoan doi 4 voi 8
# a = [6,8,4,2]

# i = 2, j in range(0,4-2-1=1)
# arr[0]=6 < arr[0+1]=8 -> True
# Hoan doi 6 voi 8

# Ouput: [8, 6, 4, 2]