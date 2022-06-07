#from owner import Owner
ID = 0

class Account:
    def __init__(self, balance):
    # def __init__(self, balance, first_name, last_name, address, telephone, email):
        if balance <= 0:
            raise Exception("Sorry, cannot create an account without a deposit")
        self.balance = balance
        self.ID = ID + 1
        # self.first_name = first_name
        #self.owner = Owner(first_name, last_name, address, telephone, email)

        def __str__(self):
            return(f"""
        Balance: {self.balance}
        """)

    def withdraw(self, debit):
        if (self.balance - debit < 0):
            print('WARNING: negative balances not permitted')
            return
        self.balance -= debit
        #return self.balance

    def deposit(self, deposit):
        self.balance += deposit



#####################
#test_account = Account(1000, 'Craig', 'Bucher', 'Chicago somewhere', '739-8994', 'craig@mail.com')
#test_account = Account(1000)

# test_account.withdraw(1001)

#print(test_account.balance)

#test_account.deposit(600)

#print(test_account.balance)