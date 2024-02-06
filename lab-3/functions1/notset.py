rlist = [1, 2, 2, 3, "aa", "aa", "suiii"]

def unique(list):
    newlist = []
    for x in list:
        if x not in newlist:
            newlist.append(x)
    return newlist

print(unique(rlist))
    