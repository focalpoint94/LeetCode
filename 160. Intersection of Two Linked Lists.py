# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        m, n = 0, 0
        cur = headA
        while cur is not None:
            m += 1
            cur = cur.next
        cur = headB
        while cur is not None:
            n += 1
            cur = cur.next
        
        if m >= n:
            for t in range(m-n):
                headA = headA.next
        else:
            for t in range(n-m):
                headB = headB.next
        
        curA, curB = headA, headB
        while curA:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None
