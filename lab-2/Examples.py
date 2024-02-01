
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print(10 + 5)

print(100 + 5 * 3)

thistuple = ("apple", "banana", "cherry")
print(thistuple)

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)