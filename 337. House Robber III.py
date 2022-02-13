# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        a, b = self.dfs(root)
        return max(a, b)
        
    def dfs(self, node):
        if not node.left and not node.right:
            return 0, node.val
        if node.left and node.right:
            a, b = self.dfs(node.left)
            c, d = self.dfs(node.right)
            return max(a+c, a+d, b+c, b+d), node.val+a+c
        if node.left:
            a, b = self.dfs(node.left)
            return max(a,b), a+node.val
        a, b = self.dfs(node.right)
        return max(a,b), a+node.val
