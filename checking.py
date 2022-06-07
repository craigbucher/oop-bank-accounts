from argparse import ArgumentError
from account import Account

class Checking(Account):
    checks = 0
    def __init__(self, balance):
        parent_instance = super()
        parent_instance.__init__(balance)
        if self.balance < 0:
            raise ValueError("Sorry, account balance can't be less than $0")

     def deposit(self, amount):
        self.balance += amount

    def withdraw(self, debit):
        if (self.balance - (debit + 1)) < 0:
            print('Sorry, account balances cannot be less than $10000')
        else:
            self.balance -= (debit + 1)
    
    def withdraw_using_check(self,amount):
        if self.checks >= 3:
            if self.balance - (amount + 2) > -10:
                self.balance -= (amount + 2)
                self.checks += 1
            else:
                print('Overdraft may not be more than -$10')
        else:
            if self.balance - amount > -10:
                self.balance -= (amount + 1)
                self.checks += 1
            else:
                print('Overdraft may not be more than -$10')
    
    def reset_checks(self):   ########## doesn't work
        self.checks = 0

testcheck = Checking(2000)
print(testcheck.balance)
testcheck.withdraw_using_check(500)
testcheck.withdraw_using_check(100)
testcheck.withdraw_using_check(100)
testcheck.withdraw_using_check(100)
print(testcheck.balance)
print(testcheck.checks)
testcheck.reset_checks
print(testcheck.checks)