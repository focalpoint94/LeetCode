# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        head, tail = self.helper(root)
        return head
        
    def helper(self, node):
        if node.left and node.right:
            ls, le = self.helper(node.left)
            rs, re = self.helper(node.right)
            node.left = ls.left = rs.left = None
            node.right = ls
            le.right = rs
            return [node, re]
        if node.left:
            ls, le = self.helper(node.left)
            node.left = ls.left = None
            node.right = ls
            return [node, le]
        if node.right:
            rs, re = self.helper(node.right)
            node.left = rs.left = None
            return [node, re]
        return [node, node]
