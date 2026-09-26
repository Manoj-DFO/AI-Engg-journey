class Node():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

node1 = Node(20)
node2 = Node(40)
node3 = Node(60)

node1.next = node2
node2.next = node3

head = node1

dummy = Node(0)
dummy.next = head

fast = dummy
slow = dummy

n = 2

for _ in range(n):
    fast = fast.next

while fast.next:
    slow = slow.next
    fast = fast.next

slow.next = slow.next.next

current = head

while current:

    print(current.data,end='->')
    current = current.next
