my_list = {
    'Iphone12': 28000000,
    'Samsung N10': 16000000,
    'Oppo 93': 7500000,
    'Vsmart': 7400000, 
    'Vivo': 4200000,
}

my_bud = int(input('Input your budget: '))

phone_list = []
for name, price in my_list.items():
    if price <= my_bud:
        phone_list.append(name)

print(phone_list)