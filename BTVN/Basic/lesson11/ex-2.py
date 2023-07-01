import os.path

my_txt = input('Input a file: ')

path = f'/Users/macbook/Documents/Python/Python/BTVN/Basic/lesson11/{my_txt}'
check_file = os.path.isfile(path)

if True:
    with open(f'/Users/macbook/Documents/Python/Python/BTVN/Basic/lesson11/{my_txt}', 'r') as name:
        print(name.read())
else:
    print('File not found')