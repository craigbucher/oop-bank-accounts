from argparse import ArgumentError
from account import Account

class MoneyMarketAccount(Account):
    transactions = 0
    def __init__(self, balance):
        parent_instance = super()
        parent_instance.__init__(balance)
        if self.balance < 10000:
            raise ValueError("Sorry, account balance can't be less than $10000")