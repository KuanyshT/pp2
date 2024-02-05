import math

class Point:
    def create(self):
        self.x1 = float(input("x1:"))
        self.y1 = float(input("y1:"))
        self.x2 = float(input("x2:"))
        self.y2 = float(input("y2:"))
        
    def show(self):
        print("(x1;y1) :", self.x1, self.y1, "(x2;y2) :", self.x2 , self.y2)
    
    def move(self):
        self.x1 = float(input("change x1:"))
        self.y1 = float(input("change y1:"))
        self.x2 = float(input("change x2:"))
        self.y2 = float(input("change y2:"))
        
    def dist(self):
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
    
obj = Point()
obj.create()
obj.show()
obj.move()
print("the distance is :" , obj.dist())
