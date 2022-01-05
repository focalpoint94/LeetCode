# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        cur, p1, p2 = dummy_head, l1, l2
        while p1 != None and p2 != None:
            if p1.val <= p2.val:
                cur.next = p1
                cur = p1
                p1 = p1.next
            else:
                cur.next = p2
                cur = p2
                p2 = p2.next
        if p1 == None:
            cur.next = p2
        else:
            cur.next = p1
        return dummy_head.next
