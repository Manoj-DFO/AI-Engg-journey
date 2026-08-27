#Bank system
class Account():
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self._balance=0

    def display(self):
        print(f'Balance: {self._balance}')

    def deposit(self,amount_add):
        self._balance = amount_add+self._balance

    def withdraw(self,withdraw_amount):
        if withdraw_amount > self._balance:
            print('Withdraw ammount exceeded, enter a valid amount')

        else:
            self._balance=self._balance - withdraw_amount
            print(f'Balance: {self._balance}')

    def __str__(self):
        return f'Name: {self.name}, ID: {self.id}, Balance: {self.balance}'

class bank():
    def __init__(self,name,city):
        self.name=name
        self.city=city
        self.dict={}

    def acc_create(self,name,id,type=''):
        if type == '' or type == 'SA':
            acc_creat=saving(name,id)
            self.dict[id]=acc_creat

        elif type == 'CA':
            acc_creat=current(name,id)
            self.dict[id]=acc_creat
        return acc_creat

    def get_acc(self,id):
        if id in self.dict:
            account=self.dict[id]
            print(f'{id}: {self.dict[id].name }')

        else:
            print('No such account')


class current(Account):
    def __init__(self,name,id):
        super().__init__(name,id)
    def withdraw(self,amount):
        balance=0
        if amount > self._balance + 1000:
            print('Amount exceded, Enter a valid amount')

        else:
            print('Withdraw sucessful ,Thank you')
            self._balance = self._balance - amount
            print(f'Balance: {self._balance}')

class saving(Account):
    def __init__(self,name,id):
        super().__init__(name,id)
    def cal_intrest(self):
        intrestrate=0.04
        intrest=self._balance*intrestrate
        self._balance=self._balance+intrest
        print(f'Total amount: {self._balance}')


b1=bank('MBI','Banglore')
b2=bank('KBI','Ramanagara')
a1=b1.acc_create('Manu',213,'CA')
a2=b1.acc_create('kumar',147)
a3=b2.acc_create('Meghana',786,'CA')
a4=b2.acc_create('Manoj',565)
print('\n')
b2.get_acc(565)
b1.get_acc(213)
a1.deposit(50000)
a3.deposit(70000)
a4.deposit(35500)
a2.display()
a4.display()
a3.withdraw(1000)