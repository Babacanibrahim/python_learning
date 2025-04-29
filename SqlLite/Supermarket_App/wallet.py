class Wallet():

    def __init__(self,balance=0):
        self.balance=balance

# Deposit
    def deposit(self,balance):
        self.balance+=balance
        print("Yeni bakiyeniz {}".format(self.balance))

# Buy product
    def buy_product(self,price):
        self.balance-=price
        print("Yeni bakiyeniz {}".format(self.balance))


# Check balance
    def check_balance(self):
        print("Bakiyeniz {} ".format(self.balance))