# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """Solution for reversing a portion of a linked list.

    Given the head of a singly linked list and two integers left and right
    (1-indexed positions), reverse the nodes from position left to right
    and return the modified list.
    """

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # Your implementation here
        # left, right are 1=indexed
        # D 1 2 3 4 5
        # 
        left_node = right_node = dummy_head = ListNode(next=head)
        prev_left_node = ListNode(next=left_node)

        for _ in range(left):
            prev_left_node = prev_left_node.next
            left_node = left_node.next
        for _ in range(right):
            right_node = right_node.next
        right_node_next = right_node.next
        
        # Cut off left<->right from the original linked list
        prev_left_node.next = None
        right_node.next = None
            
        # Reverse
        def reverse(node: ListNode) -> ListNode:
            prev = None
            while node:
                temp = node.next
                node.next = prev
                node, prev = temp, node
            return prev
        
        reversed_section_head = reverse(left_node)
        
        prev_left_node.next = reversed_section_head
        # left node has become the tail now
        left_node.next = right_node_next
        return dummy_head.next
