# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)
        
    def dfs(self, p, q):
        if not p and not q:
            return True
        if p and q:
            if p.val != q.val:
                return False
            if not self.dfs(p.left, q.left):
                return False
            if not self.dfs(p.right, q.right):
                return False
            return True
        else:
            return False
