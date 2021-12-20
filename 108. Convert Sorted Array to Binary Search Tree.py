# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.treeMaker(nums)
        
    def treeMaker(self, arr):
        if not arr:
            return None
        if len(arr) == 1:
            return TreeNode(val=arr[0])
        
        mid = len(arr) // 2
        cur = TreeNode(val=arr[mid])
        cur.left = self.treeMaker(arr[:len(arr)//2])
        cur.right = self.treeMaker(arr[len(arr)//2+1:])
        return cur
