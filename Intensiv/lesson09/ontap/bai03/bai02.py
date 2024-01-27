def fibo(n):
   if n <= 1:
       return n
   else:
       return (fibo(n-1) + fibo(n-2))

n = 5

if n <= 0:
   print("Khong thoa man")
else:
   print("Day Fibonacci:")
   for i in range(n):
       print(fibo(i))

# Nếu số thứ tự n nhỏ hơn 0 thì không thoả mãn điều kiện chạy
# dòng lặp for i để chuyển vào thuật toán fibo từng số từ 0 đến n-1
# Thuật toán sẽ dừng ở n nhỏ hơn hoặc bằng 1
# Nếu không nó sẽ chạy như sau
# Vd: 5
# for i sẽ trả về 0 -> trả về 0, vì n nhỏ hơn 1
# sau đó trả về 1 -> trả về 1, vì n bằng 1
# sau đó trả về 2 -> 2-1 + 2-2 = 1
# sau đó trả về 3 -> 3-1 + 3-2 = 3
# sau đó trả về 4 -> 4-1 + 4-2 = 5
# nó trả về lần lượt là 0, 1, 1, 3, 5