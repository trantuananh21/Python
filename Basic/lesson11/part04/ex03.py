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

# Mua hàng
my_lap = input('Input a brand: ')
my_amount = int(input('Input amount: '))

total = price[my_lap] * my_amount
print('Total price:', total)

# Tính tổng và show số lượng hàng tồn
quanity[my_lap] -= my_amount
total_items = quanity.values()
sum1 = sum(total_items)

print('Available products:')
print(quanity)
print('Total products:', sum1)