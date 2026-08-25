class product():
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'{self.name!r},{self.price}'
    
class electronicproduct(product):
    def __init__(self,brand,name,price):
        self.brand=brand
        super().__init__(name,price)

    def __str__(self):
        return f'{self.brand}-{self.name}'

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price
    
class book(product):
    def __init__(self,author,name,price):
        self.author=author
        super().__init__(name,price)

    def __str__(self):
        return f'{self.author}-{self.name}'

class shoppingcart():
    def __init__(self):
        self.lt=[]
    def add_product(self,prod):
        self.lt.append(prod)

    def rem_product(self,prod):
        self.lt.remove(prod)

    def show_product(self):
        for i in self.lt:
            print(i)

p1 = product('Laptop', 50000)
p2 = product( 'Laptop', 50000)
p3 = product('Phone', 30000)

e1 = electronicproduct('boat','earbuds',2000)
e2 = electronicproduct('noise','headphone',2500)

b1 = book('Draculla','Stars',550)
b2 = book('Manchester','Universe',700)

print(p1 == p2)
print(p1 == p3)
print(p1 is p1)
print(p1 is p2)

c1 = shoppingcart()
c1.add_product(p1)
c1.add_product(e1)
c1.rem_product(p1)
c1.add_product(p2)
c1.show_product()
print('\n')
c2 = shoppingcart()
c2.add_product(e2)
c2.add_product(b1)
c2.rem_product(e2)
c2.show_product()

print(electronicproduct.mro())