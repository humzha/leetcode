class Solution:
    """Solution for grouping odd-indexed and even-indexed nodes in a linked list.

    Given the head of a singly linked list, group all nodes with odd indices
    together followed by the nodes with even indices, and return the reordered
    list. The first node is considered odd, the second even, and so on.

    The relative order within the odd and even groups must remain the same,
    and the solution should run in O(n) time with O(1) extra space.
    """

    def oddEvenList(self, head: 'ListNode') -> 'ListNode':
        """Reorders the linked list by grouping odd-indexed nodes first.

        Args:
            head (ListNode): Head of the singly linked list.

        Returns:
            ListNode: Head of the reordered linked list.

        """
        odd_d_head = odd_tail = ListNode()
        even_d_head = even_tail = ListNode()
        
        even = True
        while head:
            temp = head.next
            if even:
                even_tail.next = head
                even_tail = even_tail.next
                even_tail.next = None
            if not even:
                odd_tail.next = head
                odd_tail = odd_tail.next
                odd_tail.next = None
            even = not even
            head = temp
        
        even_tail.next = odd_d_head.next
        return even_d_head.next
        