import datetime


n = datetime.datetime.now()

def minus5days():
    x = datetime.datetime(int(n.strftime("%Y")), int(n.strftime("%m")), abs(int(n.strftime("%d"))-5))
    print("Today is", n.strftime("%A"), ", but 5 days ago was :", x.strftime("%A")) 
    
print()
minus5days()
print()
