with open("/Users/macbook/Documents/Python/Python/Intensiv/lesson01/bai03/poem.txt") as f:
    data = [x for x in f.read().split("\n") if x.strip() != ""] 
    for line1, line2 in list(zip(data, data[1:]))[::2]:
        print(f'\t {line1}')
        print(line2)