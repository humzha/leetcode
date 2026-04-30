class Solution:
    """Solution for adding two numbers represented as reversed linked lists.

    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each node contains a single digit.

    Return the sum as a linked list in the same reversed format.
    """

    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        """Adds two numbers represented by linked lists.

        Args:
            l1 (ListNode): First number (reversed linked list).
            l2 (ListNode): Second number (reversed linked list).

        Returns:
            ListNode: Head of the linked list representing the sum.
        """
        d_head = tail = ListNode()
        carryover = False
        while l1 or l2 or carryover:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            curr_sum = (1 if carryover else 0) + l1_val + l2_val
            carryover = curr_sum >= 10

            tail.next = ListNode(curr_sum % 10)
            tail = tail.next
            tail.next = None
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return d_head.next
    