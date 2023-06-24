price = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400,
}

my_lap = input('Input a brand: ')
my_amount = int(input('Input amount: '))

total = price[my_lap] * my_amount
print('Total price:', total)