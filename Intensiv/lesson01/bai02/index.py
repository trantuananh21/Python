list = [1, 2, 3, 4, 10, 11, 20, 22, 23, 40]

even_list = []
odd_list = []
div4_list = []
prime_list = []
count = 0

for num1 in list:
    if num1 % 2 == 0:
        count += 1
        even_list.append(num1)
        final_res01 = sum(even_list) / count


for num2 in list:
    if num2 % 2 != 0:
        count += 1
        odd_list.append(num2)
        final_res02 = round(sum(odd_list) / count)
    

for num3 in list:
    if num3 % 4 == 0:
        count += 1
        div4_list.append(num3)
        final_res03 = round(sum(div4_list) / count)
    

for num4 in list:
    if num4 == 1:
        prime_list.append(num4)
    elif num4 == 2:
        prime_list.append(num4)
    elif num4 > 1:
        for i in range(2, int(num4/2)+1):
            if (num4 % i) == 0:
                break
            else:
                count += 1
                prime_list.append(num4)
                final_res04 = sum(prime_list) / count
                break

print(f'Even list: {even_list}, Sum: {final_res01}')     
print(f'Odd list: {odd_list}, Sum: {final_res02}')        
print(f'Div4 list: {div4_list}, Sum: {final_res03}')        
print(f'Prime list: {prime_list}, Sum: {final_res04}')        