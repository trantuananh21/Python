my_num = int(input('Input a number:'))
count = 0
while(my_num>0):
    count=count+1
    my_num = my_num //10
print(f"This number has {count} digit(s).")