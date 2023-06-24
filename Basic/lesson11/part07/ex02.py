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

total_skill = 0
for i in skill:
    total_skill += 1
    print(f'Skill {total_skill}: {i["Name"]}')