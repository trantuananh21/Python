print('== Input file content below ==')

txt = []

while True:
    my_input = input()

    if my_input == '':
        break
    else:
        txt.append(my_input + '\n')


with open('/Users/macbook/Documents/Python/Python/BTVN/Basic/lesson11/user-inputs.txt', 'w') as test:
    test.writelines(txt)

print('== Input recorded in user-inputs.txt ==')