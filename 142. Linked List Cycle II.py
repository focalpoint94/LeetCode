# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        met = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                met = slow
                break
        if met is None:
            return None
        slow = head
        while slow != met:
            slow = slow.next
            met = met.next
        return slow
