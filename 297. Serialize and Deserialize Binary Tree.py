# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        ret = str(root.val) + ' '
        q = [root]
        while q:
            next_q = []
            for node in q:
                if node.left:
                    next_q.append(node.left)
                    ret += str(node.left.val) + ' '
                else:
                    ret += 'null '
                if node.right:
                    next_q.append(node.right)
                    ret += str(node.right.val) + ' '
                else:
                    ret += 'null '
            q = next_q
        return ret[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        data = data.split(' ')
        root, j = TreeNode(val=int(data[0])), 1
        q = [root]
        while q:
            next_q = []
            for node in q:
                if data[j] != 'null':
                    node.left = TreeNode(val=int(data[j]))
                    next_q.append(node.left)
                j += 1
                if data[j] != 'null':
                    node.right = TreeNode(val=int(data[j]))
                    next_q.append(node.right)
                j += 1
            q = next_q
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
