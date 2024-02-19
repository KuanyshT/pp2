import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        print("x =", self.x, "y =", self.y)
        
    def move(self):
        self.x = float(input("x: "))
        self.y = float(input("y: "))
        
    def dist(self, x2, y2):
        return math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        
obj1 = Point(1, 2)
obj1.show()
print()
obj1.move()
print()
obj1.show()
print()
print(obj1.dist(3, 4))
print()

class Point3d(Point):
    def __init__(self, x, y, z):
        Point.__init__(self, x, y)
        self.z = z
        
    def show(self):
        print("x =", self.x, "y =", self.y, "z =", self.z)
        
    def move(self):
        self.x = float(input("x: "))
        self.y = float(input("y: "))
        self.z = float(input("z: "))

    def dist(self, x2, y2, z2):
        Point.dist(self, x2, y2)
        return math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2 + (z2 - self.z)**2)
    
obj2 = Point3d(3, 4, 5)
obj2.show()
print()
obj2.move()
obj2.show()
print()
print(obj2.dist(10, 11, 12))