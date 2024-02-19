import datetime

def ysandtodandtom():
    x = datetime.datetime.now()
    y = datetime.datetime(int(x.strftime("%Y")), int(x.strftime("%m")), int(x.strftime("%d")) - 1)
    tm = datetime.datetime(int(x.strftime("%Y")), int(x.strftime("%m")), int(x.strftime("%d")) + 1)
    print(y.strftime("%A"))
    print(x.strftime("%A"))
    print(tm.strftime("%A"))
    
ysandtodandtom()