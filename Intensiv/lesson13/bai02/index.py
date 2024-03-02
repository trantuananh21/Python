a = [ 1, 5, 4, 87, 4, 6, 10, 54, 21, 16, 42, 32]

# Tim kiem tuyen tinh
# x = 16 # Số cần tìm
# k = -1 # Xét xem số có nằm trong mảng hay không
# index = -1 # Vị trí của số cần tìm

# for i in a: # Vòng lặp chạy tất cả các số trong mảng
#     index += 1 # Sau mỗi lần chạy, vị trí của số cần tìm sẽ tăng lên một lần

#     if x == i: # Nếu số cần tìm và i trùng nhau

#         k = i # Số có trong mảng
#         print('So ban can tim nam o vi tri', index) # Print vị trí số cần tìm

# if k == -1: # Vì số cần tìm không có trong mảng
#     print('So ban can tim khong co trong mang') 


# Tim kiem nhi phan
def search(arr, n): # Arr là mảng, n là số cần tìm
    left = 0 # Vị trí trái trong mảng
    right = len(arr) # Vị trí bên phải trong mảng

    while left <= right: # Nếu vị trí trái nhỏ hơn hoặc bằng vị trí phải
        mid = (left+right) // 2 # Vị trí giữa của mảng

        if arr[mid] == n: # Nếu số của vị trí giữa của mảng bằng với số cần tìm
            return mid # Return vị trí của số cần tìm
        
        elif arr[mid] < n: # Nếu số của vị trí giữa của mảng nhỏ hơn số cần tìm
            left = mid + 1 # Vị trí trái bằng vị trí giữa cộng 1

        else: 
            right = mid - 1 # Vị trí phải bằng vị trí giữa trừ 1

    return -1 # Nếu không có số cần tìm trong mảng thì sẽ trả về -1

print(search(a, 16))