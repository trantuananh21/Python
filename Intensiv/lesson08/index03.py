c = [2,19,15,14,4]

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                temp = arr[j] 
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

print(bubble_sort(c))


index = -1

for i in c:
    index += 1
    
    if i % 4 == 0 and i > 0:
        print(f'Số {c[index]} nằm ở vị trí {index}')

if index == -1:
    print('Không có số chia hết cho 4 và không âm')