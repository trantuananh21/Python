# Lap trinh huong doi tuong la tao ra va truu hoa doi tuong
# Lop (class) la loai du lieu minh co the tu tao ra
# Trong lop (class) co 2 phan: method va attributes
from typing import Any


class student:
    name = 'Tran Tuan Anh'
    age = 16
    #instance


class my_homie:
    name = 'Peter'
    age = 16


class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class power_ranger:
    def __init__(self, id, colour, weight):
        self.__id = id
        self.__colour = colour
        self.__weight = weight
    
    def __getattribute__(self, __id, __colour, __weight) -> Any:
        self.id = __id 