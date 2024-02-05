class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("successfull! balance:" , self.balance)
        else:
            print("it is negative amount!")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("successfull! balance:" , self.balance)
            else:
                print("insufficient funds!")
        else:
            print("it is negative amount!")

account1 = Account("Aksha Ayan", 1000.0)

account1.deposit(500.0)
account1.withdraw(200.0)
account1.withdraw(1110000.0) 

account2 = Account("Tilenshi Kuanysh")

account2.deposit(100.0)
account2.withdraw(50.0)
account2.withdraw(-50.0)
