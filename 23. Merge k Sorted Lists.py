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
        h = [[node.val, idx, node] for idx, node in enumerate(lists) if node]
        heapq.heapify(h)
        dummy_head = ListNode()
        cur = dummy_head
        while h:
            value, idx, node = heapq.heappop(h)
            cur.next = node
            cur = node
            next_node = node.next
            if next_node:
                heapq.heappush(h, [next_node.val, idx, next_node])
        return dummy_head.next
