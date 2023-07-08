import datetime
import os
print('== Input file content below ==')

# Nhập text
txt = []

while True:
    my_input = input()

    if my_input == '':
        break
    else:
        txt.append(my_input + '\n')

path = "/Users/macbook/Documents/Python/Python/BTVN/Basic/lesson12/input-logs.txt"
# Lấy giờ
timestamp = os.path.getmtime(path)
datestamp = datetime.datetime.fromtimestamp(timestamp)


# Viết vào file
with open(path, 'a') as test:
    test.write(f'Inputs at {datestamp}\n')
    test.writelines(txt)

print('== Input recorded in input-log.txt ==')