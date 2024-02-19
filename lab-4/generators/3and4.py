n = int(input())

gen = (i for i in range(n+1) if i % 3 == 0 and i % 4 == 0)

for x in gen:
    print(x, end=" ")
    
def and34(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

gen2 = and34(n)

print()

for x in gen2:
    print(x, end=" ")