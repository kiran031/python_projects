class Bank:

    def __init__(self,name,account,min_balance):
        self.name = name
        self.account = account
        self.balance = min_balance
        print(f"Name:{self.name}\naccount:{self.account}\nmin_balance:{self.balance}")

    def deposite(self,amount):
        self.balance += amount
        print(f"your account is deposited with {amount}:balance:{self.balance}")

    def withdraw(self,amount):
        balance =self.balance-amount
        if(balance <1000):
            print(f"your account not have the sufficient money to withdra:{self.balance}")
        else:
            self.balance = balance
            print(f"your account is credited with {amount}:balance:{self.balance}")
            
        

Account = Bank("kiran","savings",min_balance = 1000)
