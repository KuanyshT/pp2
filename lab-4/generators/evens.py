n = int(input())

gen = (i for i in range(n+1) if i % 2 == 0)

lst = []

for x in gen:
    lst.append(x)
    
print (lst)