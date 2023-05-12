#  Bài 1
r = float(input("Radius: "))
pi = 3.1416
p = 2 * pi * r
s = pi * r ** 2

print(f"""
Radius: {r}
Perimeter: {p}
Area: {s}
""")


#  Bài 2
import math
lenEdge = float(input("Length of edge: "))
lenDigLine= lenEdge * math.sqrt(lenEdge)

print("Length of diagonal line:", lenDigLine)


#  Bài 3
accName = input('Account name: ')
domainName = input('Domain name: ')

print("Full email:", accName + '@' + domainName)


#  Bài 4
date1 = input("Date in MM/DD/YYYY format: ")

print('Date in DD/MM/YYYY format: ', date1[3:6:1] + date1[0:3:1] + date1[6:10:1])


#  Bài 5
deposit = float(input("Deposit: "))
interest = 105/100

afterOneYear = deposit * interest
afterTwoYears = deposit * interest**2
afterTenYears = deposit * interest**10

print(f"""
Account after 1 year: {afterOneYear}
Account after 2 years: {afterTwoYears}
Account after 10 years: {afterTenYears}
""")


#  Bài 6
import turtle as t
t.bgcolor('white')
t.shape('turtle')
t.color('#de5246')
t.pensize(7)

t.left(90)
t.forward(120)
t.right(135)
t.forward(90)
t.left(90)
t.forward(90)
t.right(135)
t.forward(120)

t.penup()
t.color('black')
t.pensize(1)
t.pendown()

t.right(90)
t.forward(130)

t.penup()
t.goto(0,120)
t.pendown()

t.right(180)
t.forward(130)

t.penup()
t.left(180)
t.forward(65)
t.right(90)
t.forward(40)

t.mainloop()

#  Bài 7
import turtle as t
t.color('#c2801d')
t.pensize(5)

t.right(45) 
t.forward(150) 
t.right(90)  
t.forward(150) 
t.right(90) 
t.forward(150) 
t.right(90) 
t.forward(150) 

t.penup()
t.color('blue')
t.goto(70,0)
t.right(90)
t.pendown()

t.forward(150) 
t.right(90)  
t.forward(150) 
t.right(90) 
t.forward(150) 
t.right(90) 
t.forward(150)  

t.mainloop()