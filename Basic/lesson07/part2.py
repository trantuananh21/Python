# 1
color = ['red', 'blue', 'green']

pos = input('Input position: ')
print(color[int(pos)-1])

# 2
color = ['red', 'blue', 'green']
print(color)

delItem = input('Item to delete: ')

if delItem.isdigit():
    color.pop(int(delItem)-1)
else:
    color.remove(delItem)

print(color)


# 3
import turtle as t
t.pensize(3)

color = ['red', 'blue', 'green']

for x in color:
    t.color(x)
    t.forward(40)
    t.penup()
    t.color(x)
    t.forward(20)
    t.pendown()


t.mainloop()