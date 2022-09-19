# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        ret = 0
        
        def dfs(node):
            if not node:
                return 'watched'
            nonlocal ret
            left, right = dfs(node.left), dfs(node.right)
            if left == 'to be watched' or right == 'to be watched':
                ret += 1
                return 'camera'
            if left == 'camera' or right == 'camera':
                return 'watched'
            if left == 'watched' and right == 'watched':
                return 'to be watched'

        state = dfs(root)
        if state == 'to be watched':
            ret += 1
        return ret
