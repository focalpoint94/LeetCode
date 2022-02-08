# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt, self.ret = 0, None
        self.dfs(root, k)
        return self.ret
        
    def dfs(self, node, k):
        if node.left:
            if self.dfs(node.left, k):
                return True 
        self.cnt += 1
        if self.cnt == k:
            self.ret = node.val
            return True
        if node.right:
            if self.dfs(node.right, k):
                return True
        return False
