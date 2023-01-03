class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def Deposit(self, amount):
        self.balance += amount

    def Withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds :(")

    def Statement(self):
        print("Account balance: ${}.".format(self.balance))


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)

    def __str__(self):
        return "{}'s current account balance: ${}".format(self.name, self.balance)

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return "{}'s savings account balance: ${}".format(self.name, self.balance)
        

# K = Current("Kayla", 500)
