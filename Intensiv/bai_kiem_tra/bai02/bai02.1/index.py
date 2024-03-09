def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)
    
n = 3
for i in range(n):
    print(recur_fibo(i))

# n là số thứ tự của dãy fibonacci
# nếu n nhỏ hơn hoặc bằng 1 thì dãy fibonacci sẽ chỉ bằng 0 hoặc không có kết quả
# còn nếu n lớn hơn 1
# Ta có dòng chạy như sau:
# Ví dụ n = 3
# recur_fibo(3) = recur_fibo(3-1=2) + recur_fibo(3-2=1)
# recur_fibo(2) = recur_fibo(2-1=1) + recur_fibo(2-2=0)
# vì n nhỏ hơn hoặc bằng 1 nên nó sẽ trả về chính nó 
# Suy ra
# recur_fibo(3) = recur_fibo(2)= 0 + 1 + recur_fibo(1)= 1
# Output: 0 ; 1; 1