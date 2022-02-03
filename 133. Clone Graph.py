"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        self.address = [False] * 101
        return self.dfs(node)
        
    def dfs(self, node):
        new_node = Node(val=node.val)
        self.address[node.val] = new_node
        
        for neighbor in node.neighbors:
            if self.address[neighbor.val] != False:
                new_node.neighbors.append(self.address[neighbor.val])
            else:
                new_node.neighbors.append(self.dfs(neighbor))
        return new_node
