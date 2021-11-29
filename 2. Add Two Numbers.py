# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
       
class Solution:
    def addTwoNumbers(self, l1, l2, up=0):
        head = ListNode()
        p1, p2 = l1, l2
        prev = head
        carry = 0
        while p1 or p2 or carry:
            if not p1:
                p1 = ListNode()
            if not p2:
                p2 = ListNode()
            val = (p1.val + p2.val + carry) % 10
            carry = (p1.val + p2.val + carry) // 10
            node = ListNode(val=val)
            prev.next = node
            prev = node
            p1 = p1.next
            p2 = p2.next
        return head.next
