# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return
        slow, fast = head, head
        intersect = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                intersect = slow
                break
        if intersect == None:
            return None
        p1, p2 = head, intersect
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
