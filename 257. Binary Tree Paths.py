# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ret = []
        self.dfs(root, [])
        return self.ret
        
    def dfs(self, node, path):
        if not node.left and not node.right:
            path.append(str(node.val))
            self.ret.append('->'.join(path))
            return
        if node.left:
            self.dfs(node.left, path+[str(node.val)])
        if node.right:
            self.dfs(node.right, path+[str(node.val)])
