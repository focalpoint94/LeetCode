# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ret = 0
        self.dfs(root, 1)
        return self.ret
        
    def dfs(self, root, height):
        self.ret = max(self.ret, height)
        if root.left:
            self.dfs(root.left, height+1)
        if root.right:
            self.dfs(root.right, height+1)
