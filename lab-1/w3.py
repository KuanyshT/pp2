#SYNTAX !!!
#exercise1
print("Hello World") 

#exercise2
if 5 > 2:
    print("YES") 
   
#COMMENTS!!!
#exercise1
#This is a comment 

#exercise2
"""
This is a comment
written in                  
more than just one line
"""

#VARIABLES!!!
#exercise1
carname = "Volvo"

#exercise2
x = 50

#exercise3
x = 5
y = 10
print(x + y)

#exercise4
x = 5
y = 10
z = x + y
print(z)

#exercise5
x , y , z = "Orange", "Banana", "Cherry"

#exercise6
x=y=z="Orange"

#exercise7
def myfunc():
  global x
  x = "fantastic"
  
#DATA TYPES
#exercise1
x = 5
print(type(x))
output : int

#exercise2
x = "Hello World"
print(type(x))
output : str    

#exercise3
x = 20.5
print(type(x))
output : float

#exercise4
x = ["apple", "banana", "cherry"]
print(type(x))
output : list

#exercise5
x = ("apple", "banana", "cherry")
print(type(x))
output : tuple

#exercise6
x = {"name" : "John", "age" : 36}
print(type(x))
output : dict

#exercise7
x = True
print(type(x))
output : bool

#NUMBERS!!!
#exercise1
x = 5
x = float(x)

#exercise2
x = 5.5
x = int(x)

#exercise3
x = 5
x = complex(x)

#STRINGS!!!
#exercise1
x = "Hello World"
print(len(x))

#exercise2
txt = "Hello World"
x = txt[0]

#exercise3
txt = "Hello World"
x = txt[2:5]

