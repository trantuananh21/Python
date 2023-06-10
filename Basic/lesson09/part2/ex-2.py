myList = [5, 1, 8, 92, -1, 30]
newList = []

while myList:
    minimum = myList[0] 
    for x in myList: 
        if x < minimum:
            minimum = x
    newList.append(minimum)
    myList.remove(minimum)    

print(newList)