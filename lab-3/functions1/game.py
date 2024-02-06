import random

print("Hello ! whats ur name?")
name = str(input("enter ur name: "))

print("Well,", name, "I am thinking of a number between 1 and 20.")
print("Take a guess.")
n = int(input("num: "))
t = random.randint(1,20)
c = 0
if n == t:
    print("Good job,", name, "! You guessed my number in 1 guess!")
else:
    c += 1
    print("you suck")
    while (n != t):
        print("Take a guess.")
        n = int(input("num: "))
        c += 1
        if n == t:
            print("Good job,", name, "! You guessed my number in", c, "guesses!")
            
            
        