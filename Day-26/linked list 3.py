class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

def delete(head,value):

    if head == None :
        return None

    if head.data == value:
        return head.next

    current = head

    while current.next is not None and current.next.data != value:
        current  = current.next

    if current.next == None:
        return head

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

head = delete(head, 390)

current = head

while current is not None:
    print(current.data, end=" → ")
    current = current.next

print("None")



#reverse
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

prev = None
current = head

while current is not None:

    next_node = current.next

    current.next = prev

    prev = current
    current = next_node


head = prev

current = head

while current is not None:
    print(current.data, end=" → ")
    current = current.next

print("None")



#middle node
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

slow = head
fast = head

def middle(slow,fast):
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

a=middle(slow,fast)

print(a.data)


#merge
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(3)
node3 = Node(5)

node1.next = node2
node2.next = node3

head1 = node1


node4 = Node(2)
node5 = Node(4)
node6 = Node(6)

node4.next = node5
node5.next = node6

head2 = node4


def merge_two_lists(list1, list2):
    dummy = Node(0)
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1

    if list2 is not None:
        current.next = list2

    return dummy.next


head = merge_two_lists(head1, head2)

current = head

while current is not None:
    print(current.data, end=" → ")
    current = current.next

print("None")