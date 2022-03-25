# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.ret = False
        self.targetSum = targetSum
        self.dfs(root, 0)
        return self.ret
        
    def dfs(self, node, sum):
        if not node.left and not node.right:
            if sum + node.val == self.targetSum:
                self.ret = True
            return
        elif node.left and not node.right:
            self.dfs(node.left, sum+node.val)
        elif not node.left and node.right:
            self.dfs(node.right, sum+node.val)
        else:
            self.dfs(node.left, sum+node.val)
            self.dfs(node.right, sum+node.val)
