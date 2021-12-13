# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ret = 0
        root_state = self.dfs(root)
        if root_state == 'should be covered':
            return self.ret + 1
        return self.ret
        
    def dfs(self, node):
        if not node:
            return 'covered'
        l, r = self.dfs(node.left), self.dfs(node.right)
        if l == 'should be covered' or r == 'should be covered':
            self.ret += 1
            return 'covering'
        if l == 'covering' or r == 'covering':
            return 'covered'
        return 'should be covered'
