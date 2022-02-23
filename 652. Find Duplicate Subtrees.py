# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.dp = {}
        self.ret = []
        self.dfs(root)
        return self.ret
        
    def dfs(self, node):
        if not node:
            return ""
        left, right = self.dfs(node.left), self.dfs(node.right)
        ret = str(node.val) + '(' + left + ')' + '(' + right + ')'
        if ret not in self.dp:
            self.dp[ret] = True
        else:
            if self.dp[ret]:
                self.ret.append(node)
                self.dp[ret] = False
        return ret
