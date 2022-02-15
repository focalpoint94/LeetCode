# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        import heapq
        h = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))
        
        head = ListNode()
        cur = head
        
        while h:
            val, i, node = heapq.heappop(h)
            cur.next = node
            cur = node
            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))
        
        return head.next
