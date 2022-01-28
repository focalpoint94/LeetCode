# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = -float('inf')
        self.dfs(root)
        return self.max
        
    def dfs(self, root):
        if not root:
            return 0
        left, right = self.dfs(root.left), self.dfs(root.right)
        ret = root.val
        if left > 0 and right > 0:
            ret += max(left, right)
        elif left > 0 and right <= 0:
            ret += left
        elif left <= 0 and right > 0:
            ret += right
        self.max = max(self.max, root.val+max(0, left)+max(0, right))
        return ret
