student1 = 'A'
student2 = 'B'

scores1 = [1,2,3,'OK', 4.5]
print(scores1)

scores2 = list(range(6))
print(scores2)

family = ['Nguyen Thanh Hien', 'Tran Manh Hung', 'Tran Hung Anh', 'Phillip Bayer', 'Emil Kierdorf']
print(family)

family = list(('Nguyen Thanh Hien', 'Tran Manh Hung', 'Tran Hung Anh', 'Phillip Bayer', 'Emil Kierdorf'))
print(family)

print(len(scores1))
print(scores1[-1])

num = [1,2,3,4,5,6,7,8,9]

# slicing
print('Slicing')
print(num[1::2])

# add
print('Add Items')
num.append(10)
print(num)

# insert
print('Insert Items')
num.insert(1, 1.5)
print(num)

# add items
print('Add items')
num.extend('ghjkl')
print(num)

# delete items
print('Delete Items')
dele = num.pop(2)
print(dele)
print(num)

# remove just one item
print('Remove Item')
num.remove(5)
print(num)

# repair items
print('Repair Items')
num[3] = 89
print(num)

# clear items
print('Clear Items')


# index
print('Index')
print(num.index(3))


# Copy string
score = [5,7,6,9,[2,3,4]]
scoreBackup = score.copy()

score[4].pop(0)
print(scoreBackup)

for name in family:
    print(name)

for x in range(len(family)):
    print(x)
    print(family[x])

for i, name in enumerate(family):
    print(i, name)


# tuple
# Mutable: can be changed: list
# Immutable: cannot be changed: string, tuple
t = (1,2,3,4,5,6)
t = tuple([7,8,9,10])
print(t)

# packing
t = (1,2,3,4,5,6)
# unpacking
a,b,c,d = (1,2,3,4)
print(a,b,c,d)

for i, val in enumerate(family):
    print(i, val)

# Excercises
# 1
print('=== Excersise 1: ===')
list1 = (1,2,3)
print(sum(list1))

# 2
print('=== Excersise 2: ===')
list2 = tuple(1,2,3,4)
print(list2[::-1])

# 3
print('=== Excersise 3: ===')
list3 = (1, 2, 3, 4, 5, 4, 5, 2, 2, 3)
newList3 = set(list3)
print(newList3)

# 4
print('=== Excersise 4: ===')
list4 = (1,2,3,4)
list5 = (3,4,5,6)

dupli = list()

for item in list4:
    if item in list5:
        dupli.append(item)

print(dupli)