orders = []

print('= Welcome to MindX Restaurant ==')

while True:
  print('Please choose a dish: ', end='')
  dish = input()

  if dish not in orders: 
    orders.append(dish)
    print('Great choice! ', end='')
  else:
    print('You chose this already. ', end='')

  print('Anything else? (y/n): ', end='')
  choice = input()
  if choice == 'n':
    break

print('Well done! Your order:')
for dish in orders:
  print('-', dish)