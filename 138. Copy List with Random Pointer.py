"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        cur, dic = head, {}
        while cur:
            dic[cur] = Node(x=cur.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                dic[cur].next = dic[cur.next]
            if cur.random:
                dic[cur].random = dic[cur.random]
            cur = cur.next
        return dic[head]
