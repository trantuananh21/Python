# Excersise 1
user = input("Input your name: ")

print('Welcome,' + ' ' + user + '!')

# Excersise 2
firstName = input('First Name: ')
lastName = input('Last Name: ')
phoneNumber = input('Phone Number: ')

print('Your registered name is' + ' ' + firstName + ' ' + lastName)
print('Your phone number is' + ' ' + phoneNumber)

# Excersise 3
print('Name \t: \t Peter \n Birthdate \t:\t  21/08/2007 ')

# Excersise 4
year = input('What year is it? ')

print("HAPPY NEW YEAR")
print('!!!' + year + "!!!")

# Excersise 5
import turtle as t
t.bgcolor('white')
t.shape('turtle')
t.fillcolor('black')

for i in range(3):
    t.forward(300)
    t.left(120)

# Excersise 6
import turtle  
ttl = turtle.Turtle()  
  
for j in range(4):  
   ttl.forward(120)  
   ttl.left(90)  
ttl.up()  
ttl.goto(9,9)  
ttl.down()  

ttl.forward(100) 
ttl.left(90) 
ttl.forward(100) 
ttl.left(90)  
ttl.forward(100) 
ttl.left(90) 
ttl.forward(100) 
ttl.left(90)   

# Excersie 7
import turtle  
ttl = turtle.Turtle()  
  
for j in range(4):  
   ttl.forward(120)  
   ttl.left(90)  
ttl.up()  
ttl.goto(60,180)  
ttl.down()  

ttl.right(45) 
ttl.forward(150) 
ttl.right(90)  
ttl.forward(150) 
ttl.right(90) 
ttl.forward(150) 
ttl.right(90) 
ttl.forward(150) 