# Thuật toán sắp xếp nổi bọt

a = [0,2,4,124,12,44,643,778,322]

for i in a:
    for j in a:
        if a[i] > a[j]:
            tam = a[i]
            a[i] = a[j]
            a[j] = tam