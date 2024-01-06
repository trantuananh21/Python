def sum_of_list(n):
    if n <= 0:
        return n
    else:
        return n + sum_of_list(n-1)
    
print(sum_of_list(3))
# Output: 6
print(sum_of_list(2))