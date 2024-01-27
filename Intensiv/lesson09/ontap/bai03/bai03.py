def sum(n):
    if n == 0:
        return n
    else:
        return n + sum(n-1)
    
print(sum(3))

# Điều kiện của thuật toán này là n phải lớn hơn 0
# Thuật toán chạy như sau:
# Ví dụ: sum(3)
# Lần đầu trả về 3
# Sau đó trả về 3 + (3-1=2)
# Sau đó trả về 3 + 2 + (2-1=1) 
# Sau đó trả về 3 + 2 + 1 + (1-1=0)
# Vì n = 0 nên chúng ta có:
# 3 + 2 + 1 + 0 = 6
# Output: 6