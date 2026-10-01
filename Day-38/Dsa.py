# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        dummy = ListNode(0)
        result = dummy
        carry = 0
        tot = 0

        while l1 or l2 or carry:

            tot = carry

            if l1:
                tot += l1.val
                l1 = l1.next

            if l2:
                tot += l2.val
                l2 = l2.next

            carry = tot // 10

            dummy.next = ListNode(tot % 10)

            dummy = dummy.next
            
        return result.next