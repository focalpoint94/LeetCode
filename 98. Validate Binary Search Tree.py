# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -float('inf'), float('inf'))
        
    def helper(self, node, mini, maxi):
        if node.val <= mini or node.val >= maxi:
            return False        
        if node.left:
            if not self.helper(node.left, mini, node.val):
                return False
        if node.right:
            if not self.helper(node.right, node.val, maxi):
                return False
        return True
