from typing import Optional, Tuple


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Given the head of a singly linked list, determine if the
        linked list is a palindrome.

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            bool: True if the list is a palindrome, False otherwise.
        """
        if not head or not head.next:
            return True

        def splice(head: Optional[ListNode]) -> Tuple[ListNode, ListNode]:
            dummy_head = slow = fast = ListNode(next=head)
            """
            D A B C D E F
            SF
              S F
                S   F
                  S     F
            D A B C D E
                  S   F
            """
            while fast and fast.next:
                slow = slow.next
                # Keep fast from overrunning, need to keep it to splice back the LL
                fast = fast.next.next if fast.next.next else fast.next
            # Two LL
            # dummy_head -> slow | (Bigger by one if odd)
            # slow.next -> fast
            head_a, head_b = dummy_head.next, slow.next
            slow.next = None
            return (head_a, head_b)

        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = temp = None
            while head:
                temp = head.next
                head.next = prev
                prev, head = head, temp
            return prev

        # List A will be greater than B by 1 if the list is odd
        head_a, head_b = splice(head)
        head_b = reverse(head_b)
        curr_a, curr_b = head_a, head_b

        is_palindrome = True
        while curr_b:
            if curr_a.val != curr_b.val:
                is_palindrome = False
                break
            curr_a = curr_a.next
            curr_b = curr_b.next

        # Connect it back together
        head_b = reverse(head_b)
        while head_a.next:
            head_a = head_a.next
        head_a.next = head_b

        return is_palindrome
