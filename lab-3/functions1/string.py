from itertools import permutations

def permut():
    s = str(input())
    perms = [''.join(p) for p in permutations(s)]
    return perms
    
print(permut())