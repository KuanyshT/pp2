class MyString:
    def getString(self):
        self.s = str(input("enter your string : "))
        
    def printString(self):
        print("this is your string :" , self.s.upper())
        
myobj = MyString()
myobj.getString()
myobj.printString()