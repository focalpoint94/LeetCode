# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.dfs(root)
        
    def dfs(self, node):
        if not node.left and not node.right:
            return 1
        if node.left and not node.right:
            return self.dfs(node.left) + 1
        if not node.left and node.right:
            return self.dfs(node.right) + 1
        left, right = self.dfs(node.left), self.dfs(node.right)
        return min(left, right) + 1
