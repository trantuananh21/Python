quanity = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

price = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400,
}

new_dict = {}

for key, value in quanity.items():
    if key in price:
        new_dict[key] = value * price[key]
    else:
        new_dict[key] = value

total_value = new_dict.values()
sum1 = sum(total_value)
print('Total value of available items:', sum1)