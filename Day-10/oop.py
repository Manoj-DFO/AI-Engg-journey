class Bankaccount:
    def __init__(self,balance,accnumber):
        self.__balance=balance
        self.__accnumber=accnumber
    def check_balance(self):
        print(f'{self.__balance} is balance')
    def deposit(self,amount):
        self.__balance+=amount
        print(f'{amount} amount is deposited ')
        print(f'{self.__balance} is balance')          #encapsulation
    def withdraw(self,withdrawl):
        self.__balance=self.__balance-withdrawl
        print(f'{withdrawl} amount withdrawed ')
        print(f'{self.__balance} is balance')
m=Bankaccount(100000,123)
c=Bankaccount(2000,234)
m.check_balance()
m.deposit(10000)
m.balance(1000)
m.withdraw(20000)
c.deposit(10000)
c.withdraw(20000)