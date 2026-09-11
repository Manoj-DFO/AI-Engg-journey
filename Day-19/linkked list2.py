#delete a number
class Node():

    def __init__(self,data):

        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1
current = head

while current.next.data != 40:
    current = current.next

current.next = current.next.next

current = head

while current is not None:
    print(current.data)
    current = current.next



#Effecient way
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def delete_node(head, value):

    # Case 1: Empty list
    if head is None:
        return head

    # Case 2: Delete head
    if head.data == value:
        return head.next

    # Find the node before the node to delete
    current = head

    while current.next is not None and current.next.data != value:
        current = current.next

    # Value not found
    if current.next is None:
        return head

    # Delete the node
    current.next = current.next.next

    return head

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

head = delete_node(head, 30)

current = head

while current is not None:
    print(current.data, end=" → ")
    current = current.next

print("None")