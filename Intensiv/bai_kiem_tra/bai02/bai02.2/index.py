def TowerOfHanoi(n , tu_cot, den_diem, phu):
    if n==1:
        print ("Chuyển 1 đĩa từ cột",tu_cot,"đến cột",den_diem)
        return
    TowerOfHanoi(n-1, tu_cot, phu, den_diem)
    print ("Chuyển đĩa",n,"từ cột",tu_cot,"đến cột",den_diem)
    TowerOfHanoi(n-1, phu, den_diem, tu_cot)
         
n = 4
TowerOfHanoi(n,'1','2','3') 