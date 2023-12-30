l = [1, 3, 8, 9, 10, 15, 41, 59, 64, 100]

def max(l):
    max = l[0]

    for i in l:
        if i > max:
            max = i

    return max

def min(l):
    min = l[0]

    for i in l:
        if i < min:
            min = i

    return min

print(l)
print('So lon nhat:', max(l))
print('So nho nhat:', min(l))
