# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.ret = []
        self.dfs(root, [], 0, targetSum)
        return self.ret
        
    def dfs(self, node, path, tempSum, targetSum):
        if not node.left and not node.right:
            if tempSum + node.val == targetSum:
                self.ret.append(path+[node.val])
            return
        if node.left:
            self.dfs(node.left, path+[node.val], tempSum+node.val, targetSum)
        if node.right:
            self.dfs(node.right, path+[node.val], tempSum+node.val, targetSum)
