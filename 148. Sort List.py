# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergesort(head)
        
    def mergesort(self, node):
        if not node or not node.next:
            return node
        slow, fast, prev = node, node, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        p1 = self.mergesort(node)
        p2 = self.mergesort(slow)
        new_head = ListNode()
        cur = new_head
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = p1
                cur = p1
                p1 = p1.next
            else:
                cur.next = p2
                cur = p2
                p2 = p2.next
        if p1:
            cur.next = p1
        else:
            cur.next = p2
        return new_head.next
