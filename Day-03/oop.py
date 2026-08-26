#Dunder methods
class CoustomList():
    def __init__(self):
        self.lt=[]

    def add(self,add):
        self.lt.append(add)

    def __str__(self):
        return str(self.lt)
    
    def __len__(self):
        return len(self.lt)
    
    def __iter__(self):
        return iter(self.lt)
    
    def __getitem__(self, index):
        return self.lt[index]

    def __lt__(self, other):
        return self.lt < other.lt

l1=CoustomList()
l2=CoustomList()
l3=CoustomList()
l4=CoustomList()
l5=CoustomList()

l1.add(23)
l2.add(35)
l2.add(35)
l2.add(40)
l2.add(50)

print(l2)
print(len(l2))
print(l2[1])
print(l1 < l2)