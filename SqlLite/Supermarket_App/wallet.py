class Wallet():

    def __init__(self,balance=0):
        self.balance=balance

# Deposit
    def deposit(self,balance):
        self.balance+=balance
        print("Yeni bakiyeniz {}".format(self.balance))

# Buy product
    def buy_product(self,price):
        if self.balance>=price:
            self.balance-=price
            print("Yeni bakiyeniz {}".format(self.balance))
        else:
            print("Yetersiz bakiye.")


# Check balance
    def check_balance(self):
        print("Bakiyeniz {} ".format(self.balance))

# Check balance after buy
    def check_balance_buy(self):
        print("Güncel Bakiyeniz {} ".format(self.balance))