# Dictionary
car = {
    'brand': 'BMW',
    'year' : 2099,
    'price': 20_000,
    'color': ['black', 'white', 'yellow']
}

# print(car['brand'])

my_self = {
    'full_name': 'Tran Tuan Anh',
    'age': 15,
    'born': 'Hanoi, Vietnam',
    'living': 'Munich, Germany',
    'language': ['Vietnamese', 'German', 'English']
}

print(f'''
Hello, my name is {my_self["full_name"]}
I'm {my_self["age"]}. 
I was born in {my_self["born"]}, but I am living in {my_self["living"]}.
I can speak {my_self["language"]}
''')

# del my_self['age']
# my_self.pop('age')
# print(len(my_self))
# my_self.clear()
# if 'age' in my_self:
#     print(my_self['age'])
# for k in my_self.keys():
#     print(k)
# for v in my_self.values():
#     print(v)
# for k, v in my_self.items():
#     print(k, '\t', v)
# print(my_self)

# def foo(*args, **kargs):
#     print(args)
#     print(kargs)
# foo(1,2,4, one=1, two=2,three=5)

# me = dict(name='Hoang', age='21')
# print(me)

# 1
# quantify = {
#     'HP': 20,
#     'DELL': 50,
#     'MACBOOK': 12,
#     'ASUS': 30
# }
# print(quantify['MACBOOK'])

# input = input('Write name of your laptop: ')
# print(quantify[input])

# 2
# character = {
#     'Name': 'Light',
#     'Age': 17,
#     'Strength': 8,
#     'Defense': 10,
#     'HP': 100,
#     'Backpack': ['Shield', 'Bread Loaf'],
#     'Gold': 100,
#     'Level': 2,
# }
# character['Gold'] += 50
# character['Backpack'].append('FlintStone')
# character.update({'Pocket': ['MonsterDex', 'Flashlight']})
# print(character)

# 3
# my_txt = input('Input a text: ')
# for i in my_txt:


def count(x):
    dict = {}
    for i in x:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

chuoi = input('Input your text: ')

dict = count(chuoi)
print(dict)
