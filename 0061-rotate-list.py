# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """Solution for rotating a linked list to the right by k places.

    Given the head of a linked list, rotate the list to the right by k places.
    """

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        # Your implementation here
        # D 1 2 3 4 5
        # k = 2
        #       s   f
        def length(head: ListNode) -> int:
            res = 0
            while head:
                res += 1
                head = head.next
            return res
        k %= length(head)
        if k == 0:
            return head
        dummy_head = slow = fast = ListNode(next=head)
        for _ in range(k):
            fast = fast.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # slow is the new tail
        # D 1 2 3 4 5
        #       s   f
        # k = 2
        #   4 5 1 2 3
        new_head = slow.next
        fast.next = dummy_head.next
        slow.next = None
        
        return new_head