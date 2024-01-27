def giai_thua(n):
    if n == 1:
        return n
    else:
        return n * giai_thua(n-1)
    
print(giai_thua(3))

# thuật toán sẽ dừng khi số n bằng 1
# nếu không thì nó sẽ chạy như sau
# n nhân với n-1
# Ví dụ:
# Lần đầu sẽ gọi 3
# Sau đó gọi 3-1 = 2
# 3 * 2
# Sau đó gọi 2-1 = 1
# Vì n lúc này bằng 1 nên sẽ dừng thuật toán
# 3 * 2 * 1 (Rút gọn)
# 3 * 2 = 6
# Output: 6