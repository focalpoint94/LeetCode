# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ret = 0
        self.k = k
        self.traverse(root)
        return self.ret
    
    # returns whether traverse should be continued
    def traverse(self, node):
        if node.left:
            if self.traverse(node.left):
                return True
        self.k -= 1
        if self.k == 0:
            self.ret = node.val
        if node.right:
            if self.traverse(node.right):
                return True
        return False
