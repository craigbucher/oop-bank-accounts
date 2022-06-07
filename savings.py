from argparse import ArgumentError
from account import Account

class Savings(Account):
    def __init__(self, balance):
        parent_instance = super()
        parent_instance.__init__(balance)
        if self.balance < 10:
            raise ValueError("Sorry, savings accounts cannot be less than $10")
        else:
            self.balance = balance
    
    def withdraw(self, debit):
        if (self.balance - (debit + 2)) < 10:
            print('Sorry, account balances cannot be less than $10')
        else:
            self.balance -= (debit +2)

    def add_interest(self, rate):
        interest = (self.balance * rate) / 100
        self.balance += interest

# test = Savings(1000)
# print(test.balance)
# test.add_interest(0.25)
# print(test.balance)