# Files
# variable_name = open('/Users/macbook/Documents/Python/Python/Basic/lesson12/file.py', mode='w')
# # do sth
# print(variable_name.write('"Hello World"'))

# variable_name.close()

# r: read
# w: write
# a: append content
# x: create new file

# with open('/Users/macbook/Documents/Python/Python/Basic/lesson12/file.py', mode='r') as file:
#     # print(file.readline()): doc dong
#     print(file.readlines(1))

with open('/Users/macbook/Documents/Python/Python/Basic/lesson12/txt.txt', mode='w') as file:
    file.writelines([
        'line1 \n'
        'line2 \n'
    ])