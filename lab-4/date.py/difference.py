import datetime

def diff(d1, d2):
    return (abs(d1 - d2)).total_seconds()

d1 = datetime.datetime(2023, 12, 5) # my birthday
d2 = datetime.datetime(2024, 2, 19) # today

print(diff(d1, d2))




    
