# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        prv, now = self.dfs(root)
        return now
        
    def dfs(self, node):
        # now: max profit until this node
        # prv: max profit until this node's children
        if not node.left and not node.right:
            prv = 0
            now = node.val
        
        elif not node.right:
            l_prv, prv = self.dfs(node.left)
            now = max(prv, l_prv+node.val)
            
        elif not node.left:
            r_prv, prv = self.dfs(node.right)
            now = max(prv, r_prv+node.val)
            
        else:
            l_prv, l_now = self.dfs(node.left)
            r_prv, r_now = self.dfs(node.right)
            prv = l_now + r_now
            now = max(prv, l_prv+r_prv+node.val)
        
        return [prv, now]
