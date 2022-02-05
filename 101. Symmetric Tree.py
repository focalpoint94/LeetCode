Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        
        if left.val != right.val:
            return False
        return self.isMirror(left.left, right.right) and \
    self.isMirror(left.right, right.left)
