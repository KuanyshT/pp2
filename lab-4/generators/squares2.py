def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
        
gen = squares(a = int(input()), b = int(input()))

for x in gen:
    print (x, end=" ")