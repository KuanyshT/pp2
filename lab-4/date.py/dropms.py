import datetime

def dropms():
    y = int(input("year:"))
    m = int(input("month:"))
    d = int(input("day:"))
    h = int(input("hours:"))
    mn = int(input("minutes:"))
    s = int(input("seconds:"))
    ms = int(input("microseconds:"))

    d1 = datetime.datetime(y, m, d, h, mn, s, ms)
    d2 = datetime.datetime(y, m, d, h, mn, s)
    
    print()
    print("your date:", d1)
    print("ms are dropped:", d2)
    print()

dropms()
