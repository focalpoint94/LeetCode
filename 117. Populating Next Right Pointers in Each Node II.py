"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.helper(root)
        return root
    
    def helper(self, leftMost):
        dummy = prev = Node()
        cur = leftMost
        while cur:
            if cur.left:
                prev.next = cur.left
                prev = cur.left
            if cur.right:
                prev.next = cur.right
                prev = cur.right
            cur = cur.next
        if dummy.next:
            self.helper(dummy.next)
