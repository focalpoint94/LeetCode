# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)
        
    def dfs(self, root, p, q):
        if not root:
            return None
        
        left, right = self.dfs(root.left, p, q), self.dfs(root.right, p, q)
        
        if root == p or root == q:
            return root
        
        if left is not None and right is not None:
            return root
        
        if left is not None:
            return left
        
        if right is not None:
            return right  
