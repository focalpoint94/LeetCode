# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ret = root.val
        
        def dfs(node):
            nonlocal ret
            if not node:
                return
            if abs(node.val - target) < abs(ret - target):
                ret = node.val
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ret
