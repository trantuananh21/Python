my_list = ['Pho', 'Bun Bo', 'Goi Cuon', 'Bun Cha']
my_order = []

print('== Welcome to MindX Restaurant ==')

order = input('Please choose a dish: ')
if order in my_list:
    my_order.append(order)
    order02 = input('Great choice! Anything else? (y/n): ')
    if order02 == 'y':
        order = input('Please choose a dish: ')
        if order not in my_order:
            my_order.append(order)
        else:
            order03 = input('You chose this already.')
        print(f'''
              Well done. Your order:
              {my_order}
              ''')
    elif order02 == 'n':
        print(f'''
              Well done. Your order is:
              {my_order}
              ''')
