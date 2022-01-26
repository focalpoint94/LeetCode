# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.builder(head)
        
    def builder(self, node):
        if not node:
            return None
        if not node.next:
            return TreeNode(val=node.val)
        prvslow, slow, fast = None, node, node
        while fast and fast.next:
            prvslow = slow
            slow = slow.next
            fast = fast.next.next
        prvslow.next = None
        new_head = TreeNode(val=slow.val)
        new_head.left = self.builder(node)
        new_head.right = self.builder(slow.next)
        return new_head
