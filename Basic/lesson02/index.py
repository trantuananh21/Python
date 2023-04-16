# Cách khai báo
myStr = 'he said:"I love you"'

print(type(myStr))

myStr2 = """
Lại rót thêm cốc bia nhưng mà lười cạn
Thành công tao đánh đổi bằng những người bạn
Thành công tao đánh đổi bằng cả hạnh phúc
Vẫn đặt lên đôi môi một nụ cười tạm
Tao chọn giữ nỗi buồn làm của riêng tao
Tao thả nó như mưa từ trên trời xuống
Chắp tay lạy phật chỉ là chiêm bao
Ngửa cổ lên trời tao được mời uống
"""

print(myStr2)



# Toán tử
myStr3 = 'Hallo'
myStr4 = 'Peter'

myStr5 = myStr3 + ' ' + myStr4
print(myStr5)

myStr6 = myStr3 * 3
print(myStr6)

firstName = input("Your First Name: ")
lastName = input('Your Last Name: ')
info = f'''
First Name: {firstName}
Last Name: {lastName}
'''

print(info)




# Cách đánh vị trí: Bắt đầu từ 0 -> độ dài -1
myStr7 = 'Hallo'
print(myStr7[4])
print(myStr7[-2])
print(myStr7[-len(myStr7)])




# Lấy chuỗi con trong string
# Slicing: start:end-1:tep
# 2:7:1 -> 2,3,4,5,6
# 2:7:2 -> 2,4,6

myStr8 = "Hallo Peter"
print(myStr8[2:7:1])
# Output: allo

k = list(range(100))
print(k[0:11:2])
# Output: 2, 4, 6, 8
print(k[::-1])
# Output: 99, 98, 97, 96,...




# Kiểu số
myStr9 = 10
print(type(myStr9)) #int

myStr10 = 10.00
print(type(myStr10)) #float

myStr11 = 4
myStr12 = 9
myStr13 = myStr11 / myStr12
print(myStr13)
print(myStr11 % myStr12) # chia lay du
print(myStr11 ** myStr12) # 4 hoch 9
print(2 ** 3 ** 2) # 2 hoch 3 hoch 2 -> 512

my_var = 10.2

int_var = int(my_var)
float_var = int(my_var)

print(int_var)
print(float_var)