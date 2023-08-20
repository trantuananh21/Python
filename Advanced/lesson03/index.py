# class nguoi :
#     def __init__(self,height,weight,skin_color):
#         self.height = height
#         self.weight = weight
#         self.skin_color = skin_color

# nguoi1 = nguoi(input("height :"),input("weight:"),input("skin color :"))
# print('Infomation for person 1')
# print(nguoi1.height)
# print(nguoi1.weight)
# print(nguoi1.skin_color)


# class dev : 
#     def __init__(self,height,weight,skin_color,position,language):
#         self.height = height
#         self.weight = weight
#         self.skin_color = skin_color
#         self.hsl = 1.02
#         self.position = position
#         self.language = language

#     def salary(self):
#         return 1000 * self.hsl

# dev1 = dev(input("height :"),input("weight :"),input("skin color :"),input("position:"),input("language :"))
# print('Infomation for dev 1')
# print(dev1.height)
# print(dev1.weight)
# print(dev1.skin_color)
# print(dev1.position)
# print(dev1.language)
# print(dev1.salary())

# class manager :
#     def __init__(self,height,weight,skin_color,position):
#         self.height = height
#         self.weight = weight
#         self.skin_color = skin_color
#         self.hsl = 1.5
#         self.position = position

#     def salary(self):
#         return 1000 * self.hsl
    
# manager1 = manager(input("height :"),input("weight :"),input("skin color :"),input("position :"))
# print('Infomation for manager 1')
# print(manager1.height)
# print(manager1.weight)
# print(manager1.skin_color)
# print(manager1.position)
# print(manager1.position)
# print(manager1.salary())

class NhanVien():
    LCB = 1000

    def __init__(self, chieu_cao, can_nang, tuoi):
        self.chieu_cao = chieu_cao
        self.can_nang = can_nang
        self.__tuoi = tuoi

    def get_private_info(self):
        return self.__tuoi
    
    def tinh_luong(self, hsl):
        return self.LCB * hsl
    
class Dev(NhanVien):
    def __init__(self, chieu_cao, can_nang, chuc_vu):
        super().__init__(chieu_cao, can_nang, 0)
        self.chuc_vu = chuc_vu

class Manager(NhanVien):
    def __init__(self, chieu_cao, can_nang, dia_chi):
        super().__init__(chieu_cao, can_nang, 0)
        self.dia_chi = dia_chi

nhanvien1 = NhanVien(1,2,3)
print(nhanvien1.get_private_info())
dev1 = Dev(1, 2, 'dev')
manager1 = Manager(3, 3, 'ko cho')

print(nhanvien1.tinh_luong(1.01))
print(dev1.tinh_luong(1.2))
print(manager1.tinh_luong(1.5))