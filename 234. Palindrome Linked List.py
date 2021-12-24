# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        fast, slow = head, head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        
        cur, prv = slow, None
        while cur:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt

        p1 = head 
        p2 = prv
        if fast == None:
            while p2:
                if p2.val != p1.val:
                    return False
                p1 = p1.next
                p2 = p2.next
            return True
        else:
            while p2.next:
                if p2.val != p1.val:
                    return False
                p1 = p1.next
                p2 = p2.next
            return True
        
