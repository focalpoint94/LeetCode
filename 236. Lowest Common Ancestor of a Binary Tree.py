# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ret = None
        self.dfs(root, p, q)
        return self.ret
    
    def dfs(self, node, p, q):
        if node == None:
            return None
        
        l = self.dfs(node.left, p, q) if node.left else None
        r = self.dfs(node.right, p, q) if node.right else None
        if (l == True) or (r == True):
            return True
            
        if node == p:
            if l == q or r == q:
                self.ret = node
                return True
            else:
                return p
        elif node == q:
            if l == p or r == p:
                self.ret = node
                return True
            else:
                return q
        elif (l == p and r == q) or (l == q and r == p):
            self.ret = node
            return True
        elif l == p or l == q:
            return l
        elif r == p or r == q:
            return r
        return None
