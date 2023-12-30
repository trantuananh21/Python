# Tim kiem tuyen tinh
l = [1, 3, 5, 7, 8, 9]
print(l)

x = int(input('So ban can tim: '))
k = -1
index = 0

for i in l:
    index += 1
    if i == x:
        k = i
        print('So ban can tim nam o vi tri', index-1)
    
if k == -1:
    print('So cua ban khong co trong list')

# dòng for i in l để xét từng chữ số trong list l, sau mỗi lần kiểm tra, index sẽ tăng thêm một đơn vị
# nếu i bằng số mình cần tìm thì sẽ trả về k = i và số mình cần tìm nằm ở vị trí index-1
# nếu i không có trong list thì dòng for sẽ không hoạt động và nó sẽ chạy dòng kiểm tra k có bằng -1 hay không,
# nếu k bằng -1 thì số của mình không có trong list