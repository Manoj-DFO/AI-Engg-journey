# class node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# node1 =  node(10)
# node2 = node(20)
# node3 = node(30)
# node4 = node(40)
# node5 = node(50)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# head = node1

# current = head

# while current is not None:
#     print(current.data, end = ' ')
#     current = current.next

# print('\n')
      
# while head is not None:
#     print(head.data, end = ' ')
#     head = head.next



class node():
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = node(10)
node2 = node(20)
node3 = node(30)
node4 = node(40)
node5 = node(50)

node1.next = node2
node3.next = node4
node2.next = node3
node4.next = node5

head = node1
current = head

while current.data != 20:
    current = current.next

new_node = node(25)

new_node.next = current.next
current.next = new_node

current = head

while current is not None:
    print(current.data,end='->')
    current = current.next
