class mySelf:
    def __init__(self, name, birth, classroom):
        self.name = name
        self.birth = birth
        self.classroom = classroom
    

tuan_anh = mySelf('Tuan Anh', 2007, '11D0')
print('Name: ', tuan_anh.name)
print('Birth: ', tuan_anh.birth)
print('Class: ', tuan_anh.classroom)