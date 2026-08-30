
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

class vehicle:
    def __init__(self, name):
        self.name = name
    def starts(self ):
        print(f'{self.name} has started.')
class bike(vehicle):                          #inheritance
    def ride(self):
        print(f'{self.name} is riding.')
b1=bike('ktm')
b2=vehicle('bmw')
b1.ride()
b2.ride()
b1.starts()
b2.starts()

class shape:
    def __init__(self):
       pass
class circle(shape):
    a=0
    def calculate_area(self,radius):
        a=3.14*radius*radius
        print(f'area of circle is {a}')        #polymorphism
class triangle(shape):
    a=0
    def calculate_area(self,length,width):
        a=length*width
        print(f'area of triangle is {a}')
c1=circle()
t1=triangle()
c1.calculate_area(4)
t1.calculate_area(4,5)