skill = [
    {
        'Name': 'Tackle',
        'Minimum level': 1,
        'Damage': 5,
        'Hit rate': 0.3,
    },

    {
        'Name': 'Quick Attack',
        'Minimum level': 2,
        'Damage': 3,
        'Hit rate': 0.5,
    },

    {
        'Name': 'Strong Kick',
        'Minimum level': 4,
        'Damage': 9,
        'Hit rate': 0.2,
    }
]
# In tổng các skill
total_skill = 0
for i in skill:
    total_skill += 1
    print(f'Skill {total_skill}: {i["Name"]}')

# Khai báo skill
my_num = int(input('Choose skill by number: '))

# Skill được chọn
choosen_skill = skill[ my_num - 1]['Name']
damage = skill[ my_num - 1]['Damage']
level = skill[ my_num - 1]['Minimum level']

# In skill được chọn
print(f'You chose {choosen_skill}')

# Kiểm tra level
if level <= my_num:
    print('Damage:', damage)
else:
    print('Cannot deploy. Required level 4.')