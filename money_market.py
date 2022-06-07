from argparse import ArgumentError
from account import Account

class MoneyMarketAccount(Account):
    transactions = 0
    low_balance = False
    def __init__(self, balance):
        parent_instance = super()
        parent_instance.__init__(balance)
        if self.balance < 10000:
            raise ValueError("Sorry, account balance can't be less than $10000")
    
    def withdraw(self, debit):
        if self.transactions < 6:
            if not(self.low_balance):
                if (self.balance - debit ) < 10000:
                    print('Balance less than $10000; $100 fee and no more transactions')
                    self.low_balance = True
                    self.balance -= debit + 100
                    self.transactions += 1
                else:
                    self.balance -= debit
                    self.transactions += 1
            else:
                print('Account below minimum; no transactions until above $10000')
        else:
            print('Maximum number of transactions (6) reached')

    def deposit(self, amount):
        if self.transactions < 6:
            if self.low_balance:
                self.balance += amount
            else:
                self.balance += amount
                self.transactions += 1
        else:
            print('Maximum number of transactions (6) reached')
    
    def add_interest(self, rate):
        interest = (self.balance * rate) / 100
        self.balance += interest

    def reset_transactions(self):
        self.transactions = 0    ########## Doesn't work

money = MoneyMarketAccount(20000)
print(money.balance)
money.withdraw(1000)
print(money.transactions)
money.withdraw(1000)
print(money.transactions)
money.withdraw(1000)
print(money.transactions)
money.withdraw(1000)
print(money.transactions)
money.withdraw(1000)
print(money.transactions)
money.withdraw(1000)
print(money.transactions)
print(money.balance)
money.withdraw(1000)
print(money.transactions)
print(money.balance)
money.reset_transactions
print(money.transactions)