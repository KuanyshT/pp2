class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

obj1 = Shape()
obj2 = Square(5)         

print(obj1.area())
print(obj2.area())

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.width * self.length
    
obj3 = Rectangle(5, 4)

print(obj3.area())