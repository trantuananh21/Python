# Tìm kiếm nhị phân
def search(arr, n):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left+right) // 2

        if arr[mid] == n:
            return mid
        
        elif arr[mid] < n:
            left = mid + 1

        else:
            right = mid - 1

    return -1

l = [1, 3, 5, 7, 8, 9]
print(l)

x = int(input('So ban can tim: '))

print(search(l, x))

# phương thức search sẽ có 2 arguments: arr và n
# arr là list số và n là số mình cần tìm
# đầu tiên là phải định nghĩa số trái và số phải
# số trái sẽ bằng 0 và số phải sẽ bằng độ dài của list -1 

# nếu số trái nhỏ hơn hoặc bằng số phải thì sẽ chạy vòng lặp while
# số ở giữa sẽ bằng số trái cộng số phải chia đôi
# nếu vị trí số ở giữa ở trong list có bằng số mìh cần tìm thì sẽ trả về số mình cần tìm
# nếu không thì sẽ chạy thêm một dòng kiểm tra vị trí số mình cần tìm trong list có nhỏ hơn số mình cần tìm hay không
# thì sẽ trả về số bên trái bằng số ở giữa cộng 1
# còn lại thì sẽ trả về số bên phải bằng số ở giữa trừ 1

# nếu số mình cần tìm không có trong list thì sẽ trả về -1