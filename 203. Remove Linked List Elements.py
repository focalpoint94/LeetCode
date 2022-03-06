# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head = ListNode(val=0, next=head)
        prv, cur = new_head, head
        while cur:
            if cur.val == val:
                prv.next = cur.next
                cur = cur.next
            else:
                prv = cur
                cur = cur.next
        return new_head.next
