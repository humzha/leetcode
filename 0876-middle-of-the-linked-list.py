class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a singly linked list, return the middle
        node of the linked list. If there are two middle nodes,
        return the second middle node.

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            Optional[ListNode]: The middle node of the linked list.

        DUMMY -> A -> B -> C -> D -> E -> F
        SF
                 s    F
                      s         F
                           s              F

        EVEN, F is the tail
        RETURN S.NEXT

        DUMMY -> A -> B -> C -> D -> E
        SF
                 s    F
                      s         F

        ODD, F is None
        RETURN S
        """
        if not head or not head.next:
            return head

        dummy_head = tail = ListNode(next=head)
        s = f = dummy_head
        while f and f.next:
            s = s.next
            f = f.next.next
        if f is None:
            return s
        return s.next
