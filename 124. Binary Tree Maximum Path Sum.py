# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ret = -float('inf')
        self.dfs(root)
        return self.ret
        
    def dfs(self, node):
        if not node:
            return 0
        left, right = self.dfs(node.left), self.dfs(node.right)
        self.ret = max(self.ret, node.val, node.val+left, node.val+right, node.val+left+right)
        return max(node.val, node.val+left, node.val+right)
