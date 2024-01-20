a = [1,5,4,7,0]

# Bubble Sort
# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 temp = arr[j] 
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp

#     return arr

# print(bubble_sort(a))


# Giải thích:
# n là độ dài của list mình được cho
# chạy vòng lặp for i trong vòng từ 0 đến độ dài của list
# trong vòng lặp for i sẽ có vòng lặp for j từ 0 đến n-i-1
# nếu số thứ tự của số j lớn thơn số thứ tự của số j+1 thì sẽ đổi chỗ hai số
# nếu không có gì thì sẽ không thay đổi
# chạy xong dòng j thì i sẽ tăng lên một
# i sẽ chạy đến khi nào không đạt điều kiện i<n thì dừng

# Vdu:
# a = [1,5,4,7,0]
# i = 0 và n = 5
# j sẽ chạy từ 0 cho đến 5-0-1=4
# arr[0]=1 > arr[0+1=1]=5 -> Sai, không thay đổi
# arr[1]=5 > arr[2+1=2]=4 -> Đúng, đổi chỗ 4 với 5
# list mới: a = [1,4,5,7,0]
# arr[2]=5 > arr[2+1=3]=7 -> Sai, không thay đổi
# arr[3]=7 > arr[3+1=4]=0 -> Đúng, đổi chỗ 7 và 0
# list mới: a = [1,4,5,0,7]


# Selection Sort
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

print(sel_sort(a))


# Giải thích:
# n là độ dài của list
# vòng lặp for i có độ dài từ 0 đến n-1
# min = i với min là số nhỏ nhất
# trong vòng lặp for i sẽ có vòng lặp for j có độ dài từ i đến n
# nếu số j nhỏ hơn số min là số nhỏ nhất thì min = j
# chạy xong vòng j, chúng ta sẽ kiểm tra xem min có bằng i không
# nếu i khác min thì min với i sẽ đổi chỗ cho nhau trong list

# Ví dụ:
# a = [1,5,4,7,0]
# i = 0 và n = 5
# min = i = 0
# j sẽ chạy từ 0 đến 4
# arr[0]=1 < arr[0]=1 -> Sai, không thay đổi
# arr[1]=5 < arr[0]=1 -> Sai, không thay đổi
# arr[2]=4 < arr[0]=1 -> Sai, không thay đổi
# arr[3]=7 < arr[0]=1 -> Sai, không thay đổi
# arr[4]=0 < arr[0]=1 -> Đúng, min = j = 4

# Vì min khác i nên đổi chỗ 0 với 1
# list mới: a = [0,5,4,7,1]


# Tim kiem tuyen tinh
# x = 7
# index = -1

# for i in a:
#     index += 1

#     if i == x:
#         print('So cua ban nam o vi tri', index)

# if index == -1:
#     print('So cua ban khong duoc tim thay')


# Giải thích:
# x là số cần tìm vị trí
# index là số thứ tự của số cần tìm
# chạy vòng lặp i trong list a để duyệt từng chữ số một trong list a
# sau mỗi lần chạy, index sẽ cộng thêm 1
# nếu i bằng số cần tìm, nó sẽ trả về thứ tự của số cần tìm trong list đó
# nếu chạy xong hết vòng lặp i mà i không bằng số cần tìm thì sẽ chạy dòng nếu index giữ nguyên
# thì sẽ trả lại rằng số cần tìm không có trong list

# Ví dụ:
# a = [0, 1, 4, 5, 7]
# x = 1
# i đầu tiên sẽ bằng 0, index sẽ cộng thêm 1(-1+1=0), vì 0 khác 1 nên sẽ chạy tiếp 
# i tiếp theo sẽ bằng 1, index sẽ cộng thêm 1(0+1=1), vì 1 bằng 1 nên sẽ trả về index
# lúc này index bằng 1 nên vị trí số 1 trong list là 1


# Tim kiem nhi phan
def bin_search(arr, n):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == n:
            return mid
        
        elif arr[mid] <= n:
            left = mid + 1

        else:
            right = mid - 1

    return -1

print('So cua ban nam o vi tri', bin_search(a,7))


# Giải thích:
# n là số chúng ta cần tìm
# số bên trái bằng 0
# số bên phải bằng độ dài của list đó trừ 1
# nếu số bên trái nhỏ hơn hoặc bằng số bên phải thì sẽ chạy dòng ở dưới đây
# số ở giữa sẽ bằng số bên trái cộng số bên phải và chia lấy nguyên cho 2
# nếu số ở giữa bằng với n thì sẽ trả về số đó
# nếu số ở giữa nhỏ hơn số n thì số bên trái sẽ bằng số ở giữa cộng với 1
# vì số bên trái cần phải lớn hơn để cắt ngắn lại độ dài của số bên trái với số bên phải
# nếu số ở ở giữa lớn hơn số n thì số bên phải sẽ bằng số ở giữa trừ 1
# vì số bên phải cần phải nhỏ hơn để cắt ngắn lại độ dài của số bên trái với số bên phải

# Ví dụ:
# a = [0, 1, 4, 5, 7]
# n = 5
# left = 0
# right = 4
# vì số bên trái nhỏ hơn số bên phải
# nên ta chạy dòng tiếp theo để tính số ở giữa
# số ở giữa sẽ bằng (0+4) chia lấy nguyên cho 2 bằng 2
# vì arr[2]=4 < 5 nên số bên trái sẽ bằng 2+1=3

# số ở giữa sẽ bằng (3+5) chia lấy nguyên cho 2 bằng 4
# vì arr[4]=7 > 5 nên số bên phải sẽ bằng 4-1=3

# số ở giữa sẽ bằng (3+3) chia lấy nguyên cho 2 bằng 3
# vì arr[3]=5 = 5 nên vị trí số cần tìm là 3

