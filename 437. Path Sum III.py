from collections import Counter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        self.target = targetSum
        self.counter, self.ret = Counter(), 0
        self.dfs(root, 0)
        return self.ret
        
    def dfs(self, node, culm):
        if not node:
            return
        culm += node.val
        if culm == self.target:
            self.ret += 1
        self.ret += self.counter[culm-self.target]
        self.counter[culm] += 1
        self.dfs(node.left, culm)
        self.dfs(node.right, culm)
        self.counter[culm] -= 1



# from collections import Counter
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         if not root:
#             return 0
#         self.ret = 0
#         self.target = targetSum
#         self.dfs(root)
#         return self.ret
        
#     def dfs(self, node):
#         counter = Counter()
#         if node.val == self.target:
#             self.ret += 1
#         counter[node.val] = 1
#         if not node.left and not node.right:
#             return counter
#         if node.left:
#             lCounter = self.dfs(node.left)
#             self.ret += lCounter[self.target-node.val]
#             for key, val in lCounter.items():
#                 counter[key+node.val] += val
#         if node.right:
#             rCounter = self.dfs(node.right)
#             self.ret += rCounter[self.target-node.val]
#             for key, val in rCounter.items():
#                 counter[key+node.val] += val
#         return counter
