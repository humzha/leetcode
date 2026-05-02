class Solution:
    """Solution for reordering a linked list.

    Given the head of a singly linked list:
    L0 → L1 → … → Ln

    Reorder it to:
    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

    You must do this in-place without modifying node values.
    """

    def reorderList(self, head: 'ListNode') -> None:
        """Reorders the linked list in-place.

        Args:
            head (ListNode): Head of the linked list.

        Returns:
            None
        """
        # D 1 2 3 4 5
        # sf
        #   s f
        #     s   f
        #       s   f
        # D 1 2 3 4 5
        
        # Split head
        d_head = slow = fast =  ListNode(next=head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next
        split_head = slow.next
        slow.next = None

        # Reverse second half
        def reverse(head: ListNode):
            if not head:
                return None
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev, head = head, temp 
            return prev

        split_head = reverse(split_head)
        
        res_d_head = tail = ListNode()
        
        a, b = d_head.next, split_head
        # |a| is at most 1 greater than |b|
        a_turn = True
        while a or b:
            if a_turn:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
            tail.next = None
            a_turn = not a_turn
            
        return res_d_head.next
