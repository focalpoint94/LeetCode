# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur != None:
            length += 1
            cur = cur.next
        prv, cur = None, head
        num_move = length - n
        while num_move > 0:
            prv = cur
            cur = cur.next
            num_move -= 1
        if cur == head:
            return head.next
        prv.next = cur.next
        return head
