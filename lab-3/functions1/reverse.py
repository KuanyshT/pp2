def rvrs():
    s = str(input())
    l = s.split()
    for i in range(-1, -len(l) - 1, -1):
        print(l[i] , end= " ")

rvrs()
