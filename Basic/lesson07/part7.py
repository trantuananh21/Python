# 1
scores = [78, 56, 67]

# 2
print('High scores:')
for i, name in enumerate(scores):
    print(f'''{i+1}. {name}''')

# 3
newScore = int(input('Input new score: '))
scores.append(newScore)
for i, name in enumerate(scores):
    print(f'''{i+1}. {name}''')