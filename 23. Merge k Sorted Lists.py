# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = head = ListNode()
        
        h = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))
        
        while h:
            val, i, node = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))
            
        return head.next
