my_list = {
    'Iphone12': 28000000,
    'Samsung N10': 16000000,
    'Oppo 93': 7500000,
    'Vsmart': 7400000, 
    'Vivo': 4200000,
}

my_txt = input('Input name of a phone: ')

price = my_list[my_txt]
print(f'Price of {my_txt}: {price}')