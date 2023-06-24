quanity = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

my_lap = input('Input a brand: ')
my_amount = input('Input amount: ')

quanity.update({ my_lap : my_amount})
print(quanity)