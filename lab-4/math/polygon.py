import math
def convert(d):
    return d/180 * math.pi

def area():
    n = int(input("sides: "))
    l = float(input("length of sides: "))
    return l**2 * n / (4 * math.tan(convert(180/n)))

print(area())