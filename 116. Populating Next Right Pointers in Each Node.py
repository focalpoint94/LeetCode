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
        if not root:
            return
        self.node_address = [None] * 12
        self.dfs(root, 0)
        return root
        
    def dfs(self, node, height):
        if node == None:
            return
        if self.node_address[height] == None:
            self.node_address[height] = node
        else:
            self.node_address[height].next = node
            self.node_address[height] = node
        self.dfs(node.left, height+1)
        self.dfs(node.right, height+1)
        
