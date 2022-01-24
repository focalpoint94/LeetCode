# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        new_head = ListNode()
        cur, val, freq = head, None, 0
        node_ptr = new_head
        while cur != None:
            if cur.val != val:
                if freq == 1:
                    new_node = ListNode(val=val)
                    node_ptr.next = new_node
                    node_ptr = new_node
                val, freq = cur.val, 1
            else:
                freq += 1
            cur = cur.next
        if freq == 1:
            node_ptr.next = ListNode(val=val)
        return new_head.next
