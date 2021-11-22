class Solution:
    def reorderList(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        new_head = slow.next
        slow.next = None
        
        cur, prev = new_head, None
        while cur:
            nextt = cur.next
            cur.next = prev
            prev = cur
            cur = nextt
        new_head = prev
        
        head1, head2 = head, new_head
        while head2:
            next1 = head1.next
            head1.next = head2
            next2 = head2.next
            head2.next = next1
            head1 = next1
            head2 = next2
        return head
