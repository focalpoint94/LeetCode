# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'N'
        return '.'.join([str(root.val), self.serialize(root.left), self.serialize(root.right)]) 
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split('.')
        data = deque(data)
        
        def helper():
            value = data.popleft()
            if value == 'N':
                return None
            node = TreeNode(value)
            node.left = helper()
            node.right = helper()
            return node
        
        return helper()
        
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
