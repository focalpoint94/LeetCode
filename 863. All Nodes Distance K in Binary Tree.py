# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, par=None):
            if node:
                node.parent = par
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        
        ret = []
        
        q = deque()
        q.append((target, 0))
        visited = {target}
        while q:
            u, d = q.popleft()
            if d > k:
                continue
            if d == k:
                ret.append(u.val)
                continue
            for nei in (u.left, u.right, u.parent):
                if nei and nei not in visited:
                    q.append((nei, d+1))
                    visited.add(nei)
        return ret
