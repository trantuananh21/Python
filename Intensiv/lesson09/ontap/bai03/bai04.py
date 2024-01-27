def luy_thua(x,n):
    if n == 0:
        return 1
    else:
        return x * luy_thua(x, n-1)
    
print(luy_thua(3,2))

# Điều kiện của thuật toán là số mũ luôn phải lớn hơn 0
# Thuật toán chạy như sau
# Ví dụ 3 mũ 2
# Đầu tiên nó sẽ trả về 3 * (3,2-1=1)
# Sau đó nó sẽ trả về 3 * (3,2-1=1) * (3,1-1=0)
# Sau đó dừng vì n bằng 0
# Chúng ta có 3 * (3**1 * 3**0) = 9
# Output: 9 
