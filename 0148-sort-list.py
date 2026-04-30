class Solution:
    """Solution for sorting a linked list in ascending order.

    Given the head of a singly linked list, return the list after sorting it
    in ascending order. The values must be rearranged by modifying node links,
    not by changing node values.
    """

    def sortList(self, head: 'ListNode') -> 'ListNode':
        """Sorts a singly linked list in ascending order.

        Args:
            head (ListNode): Head of the linked list.

        Returns:
            ListNode: Head of the sorted linked list.
        """
        def split(head: 'ListNode') -> 'ListNode':
            if not head:
                raise ValueError()
            dummy_head = ListNode(next=head)
            slow = fast = dummy_head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next if fast.next else fast.next
            split_head = slow.next
            slow.next = None
            return split_head
        
        def merge(a: 'ListNode', b: 'ListNode') -> 'ListNode':
            if not a or not b:
                raise ValueError()
            dummy_head = tail = ListNode(next=head)
            while a or b:
                if a and not b:
                    tail.next = a
                    break
                if b and not a:
                    tail.next = b
                    break

                if a.val < b.val:
                    temp = a.next

                    tail.next = a
                    tail = tail.next
                    tail.next = None 

                    a = temp
                else:
                    temp = b.next

                    tail.next = b
                    tail = tail.next
                    tail.next = None 

                    b = temp
            return dummy_head.next

        def merge_sort(head: 'ListNode') -> 'ListNode' | None:
            if not head or not head.next:
                return head
            b = merge_sort(split(head))
            a = merge_sort(head)
            
            return merge(a, b)
    
        return merge_sort(head)