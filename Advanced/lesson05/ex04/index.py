class Cha:
    def __init__(self, name, birth, adress):
        self.name = name
        self.birth = birth
        self.adress = adress

    def input():
        name = input('Name: ')
        birth = input('Birth: ')
        adress = input('adress: ')

        cha01 = Cha(name, birth, adress)
        

class NguoiDan(Cha):
    def __init__(self, name, birth, adress, position):
        super().__init__(name, birth, adress)
        self.position = position
        self.hsl = 4.5 
    LCB = 1000

    def tinh_luong(self):
        return self.LCB * self.hsl

class CanBo(Cha):
    LCB = 1000
    def __init__(self, name, birth, adress, hoc_ham, hoc_vi):
        super().__init__(name, birth, adress)
        self.hoc_ham = hoc_ham
        self.hoc_vi = hoc_vi
        self.hsl = 8.3

    def tinh_luong(self):
        return self.LCB * self.hsl
    
print('Cha')
cha01 = Cha(input('Name: '), input('Birth: '), input('Adress: '))
print('\n')
print('Name: ', cha01.name)
print('Birth: ', cha01.birth)
print('Adress: ', cha01.adress)

print('\n')
ng_dan01 = NguoiDan(input('Name: '), input('Birth: '), input('Adress: '), input('Position: '))
print('\n')
print('Name: ', ng_dan01.name)
print('Birth: ', ng_dan01.birth)
print('Adress: ', ng_dan01.adress)
print('Position: ', ng_dan01.position)
print('Luong: ', ng_dan01.tinh_luong())

print('\n')
can_bo01 = CanBo(input('Name: '), input('Birth: '), input('Adress: '), input('Hoc ham: '), input('Hoc ham: '))
print('\n')
print('Name: ', can_bo01.name)
print('Birth: ', can_bo01.birth)
print('Adress: ', can_bo01.adress)
print('Hoc ham: ', can_bo01.hoc_ham)
print('Hoc vi: ', can_bo01.hoc_vi)
print('Luong: ', can_bo01.tinh_luong())