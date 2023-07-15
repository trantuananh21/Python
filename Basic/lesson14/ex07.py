my_list = [5, 1, 8, 92, -1, 30]

print(f'''
Original list:
{my_list}
''')

new_list = []

while my_list:
    minimum = my_list[0]
    for x in my_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    my_list.remove(minimum)    

print(f'''
Sorted list:
{new_list}
''')
