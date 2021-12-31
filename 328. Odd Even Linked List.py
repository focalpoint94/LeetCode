# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd_ptr = head
        even_ptr = even_head = ListNode()
        cur = head.next
        cnt = 2
        while cur != None:
            if cnt % 2 != 0:
                odd_ptr.next = cur
                odd_ptr = cur
            else:
                even_ptr.next = cur
                even_ptr = cur
            cur = cur.next
            cnt += 1
        even_ptr.next = None
        odd_ptr.next = even_head.next
        return head
        
