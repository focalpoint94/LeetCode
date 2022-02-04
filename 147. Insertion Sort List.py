# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        dummy_head = ListNode(val=0, next=head)
        prev, cur = head, head.next
        while cur:
            nxt = cur.next
            p1, p2 = dummy_head.next, dummy_head
            while p1.val < cur.val:
                p1 = p1.next
                p2 = p2.next
            if p1 == cur:
                prev = cur
                cur = nxt
            else:
                prev.next = nxt
                p2.next = cur
                cur.next = p1
                cur = nxt
        return dummy_head.next
