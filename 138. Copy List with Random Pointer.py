"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ptr = new_head = Node(x=0)
        
        cur = head
        while cur:
            nxt = cur.next
            ptr.next = Node(cur.val, None, cur.random)
            cur.next = ptr.next
            ptr = ptr.next
            cur = nxt
        
        ptr = new_head.next
        while ptr:
            ptr.random = ptr.random.next if ptr.random else None
            ptr = ptr.next
        return new_head.next
