# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        
        count, cur, prv = 0, head, None
        while cur != None:
            prv = cur
            count += 1
            cur = cur.next
            
        tail = prv
        
        k %= count
        if k == 0:
            return head
        
        cur = head
        for i in range(count - k - 1):
            cur = cur.next
        
        new_head = cur.next
        cur.next = None
        tail.next = head
        return new_head
