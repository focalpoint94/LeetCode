# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ret = []
        self.dfs(root)
        return self.ret
        
    def dfs(self, node):
        if node.left and node.right:
            h = max(self.dfs(node.left), self.dfs(node.right)) + 1
        elif node.left:
            h = self.dfs(node.left) + 1
        elif node.right:
            h = self.dfs(node.right) + 1
        else:
            h = 0
        if h == len(self.ret):
            self.ret.append([])
        self.ret[h].append(node.val)
        return h
