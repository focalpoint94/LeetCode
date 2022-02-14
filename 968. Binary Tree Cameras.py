# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ret = 0
        if self.dfs(root) == 'to be covered':
            self.ret += 1
        return self.ret
        
    def dfs(self, node):
        if not node.left and not node.right:
            return 'to be covered'
        if node.left and not node.right:
            left = self.dfs(node.left)
            if left == 'covered':
                return 'to be covered'
            if left == 'cam':
                return 'covered'
            if left == 'to be covered':
                self.ret += 1
                return 'cam'
        if not node.left and node.right:
            right = self.dfs(node.right)
            if right == 'covered':
                return 'to be covered'
            if right == 'cam':
                return 'covered'
            if right == 'to be covered':
                self.ret += 1
                return 'cam'
        left, right = self.dfs(node.left), self.dfs(node.right)
        if left == 'to be covered' or right == 'to be covered':
            self.ret += 1
            return 'cam'
        if left == 'cam' or right == 'cam':
            return 'covered'
        return 'to be covered'
