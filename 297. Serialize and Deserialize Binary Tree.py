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
            return ''
        data = ''
        
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                data += 'N,'
            else:
                data += str(node.val) + ','
                q.append(node.left)
                q.append(node.right)
        return data[:-1]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        head = TreeNode(int(data[0]))
        ptr = 1
        q = deque()
        q.append(head)
        while q:
            node = q.popleft()
            if node:
                if data[ptr] != 'N':
                    node.left = TreeNode(int(data[ptr]))
                ptr += 1
                if data[ptr] != 'N':
                    node.right = TreeNode(int(data[ptr]))
                ptr += 1
                q.append(node.left)
                q.append(node.right)
        return head

       

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
