class Solution:
    """Solution for swapping every two adjacent nodes in a linked list.

    Given a linked list, swap every two adjacent nodes and return its head.
    You must swap the nodes themselves, not just their values.
    """

    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        """Swaps nodes in pairs throughout the linked list.

        Args:
            head (ListNode): Head of the singly linked list.

        Returns:
            ListNode: Head of the modified list after pairwise swaps.
        """
        d_head = ListNode()
        d_head.next = head
        res_d_head = res_tail = ListNode()

        # consume chunks of a, b or just a
        # the first two from the listnode
        while d_head.next is not None:
            a = d_head.next
            b = d_head.next.next

            # Iterate forward the LL pointer by two
            if b:
                d_head.next = b.next
            # if b doesn't exist, no more nodes can be consumed/swapped
            else:
                d_head.next = None
            
            # Even
            if not b:
                res_tail.next = a
                res_tail = res_tail.next
            # General Case
            else:
                res_tail.next = b
                res_tail = res_tail.next
                res_tail.next = a
                res_tail = res_tail.next
            res_tail.next = None
        return res_d_head.next