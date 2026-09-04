#Create a Python Employee Management System using all 4 pillars of OOP with Getter and Setter method.
from abc import ABC,abstractmethod
class employee(ABC):
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative")
    @abstractmethod
    def calculate_bonus(self):
        pass

class developer(employee):
    def calculate_bonus(self):
        return self.get_salary()*0.2

class manager(employee):
    def calculate_bonus(self):
        return self.get_salary()*0.3


d1 = developer("Manoj", 50000)
m1 = manager("Rahul", 70000)

print(d1.name)
print(d1.get_salary())
print(d1.calculate_bonus())

print(m1.name)
print(m1.get_salary())
print(m1.calculate_bonus())

d1.set_salary(60000)
print(d1.get_salary())

d1.set_salary(-5000)