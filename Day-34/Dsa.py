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
class Solution(object):
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next