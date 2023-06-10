# Phần 3 này em chưa làm được ạ
import os
import getch

mapS = [5, 5]

objects = {}

def mapSize(x, y):
    global mapS
    mapS = [x, y]

def addObject(name, x, y, symbol):
    objects[name] = [x, y, symbol]

addObject("Player", 1, 1, "P ")
addObject("Key", 4, 3, "K ")
addObject("Door", 1, 5, "D ")

for y in range(mapS[1]):
    line = ""
    numy = y+1
    for x in range(mapS[0]):
        numx = x + 1
        for place in objects:
            if objects[place][:2] == [numx, numy]:
                line += objects[place][2]
                break
        else:
            line += "- "        
    print(line)


print('''
== THE ESCAPE GAME ==
Use W A S D to move the (P)layer
Find (K)ey then exit through the (D)oor
''')