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
        
    def helper(self, node):
        if not node:
            return
        leftmost, prev = None, None
        cur = node
        while cur:
            if cur.left:
                if not leftmost:
                    leftmost, prev = cur.left, cur.left
                else:
                    prev.next = cur.left
                    prev = cur.left
            if cur.right:
                if not leftmost:
                    leftmost, prev = cur.right, cur.right
                else:
                    prev.next = cur.right
                    prev = cur.right
            cur = cur.next   
        self.helper(leftmost)
