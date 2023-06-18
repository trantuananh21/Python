def count(x):
    dict = {}
    for i in x:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

chuoi = input('Input sequence: ')

dict = count(chuoi)
print('Frequency of characters:\n ', dict)
