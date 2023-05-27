# 1
scores = [78, 56, 67]

newScore = int(input('Input new score: '))

scores.append(newScore)
scores.sort(reverse = True)

for i, name in enumerate(scores):
    print(f'''{i+1}. {name}''')

# 2
scores2 = [78, 70, 67, 56, 45]
newScore2 = int(input('Input new score: '))

scores2.append(newScore2)
scores2.sort(reverse = True)


for i, name in enumerate(scores2):
    if i < 5:
        print(f'''{i+1}. {name}''')

