# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        ret = None
        def inorder(node):
            nonlocal ret
            if node.left:
                inorder(node.left)
            if ret is None and node.val > p.val:
                ret = node
            if node.right:
                inorder(node.right)
        inorder(root)
        return ret
