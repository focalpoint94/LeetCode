# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.startValue, self.destValue = startValue, destValue
        LCA = self.findLCA(root)
        self.path1, self.path2 = '', ''
        stack = [(LCA, '')]
        while stack:
            node, path = stack.pop()
            if node.val == startValue:
                self.path1 = 'U' * len(path)
            elif node.val == destValue:
                self.path2 = path
            if node.left: stack.append((node.left, path+'L'))
            if node.right: stack.append((node.right, path+'R'))
        return self.path1 + self.path2
        
    def findLCA(self, node):
        if not node:
            return None
        if node.val == self.startValue or node.val == self.destValue:
            return node
        left, right = self.findLCA(node.left), self.findLCA(node.right)
        if left and right:
            return node
        if left:
            return left
        if right:
            return right
