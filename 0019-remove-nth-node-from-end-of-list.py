# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = fast = slow = ListNode(next=head)
        
        # 1 <= n <= sz
        for _ in range(n):
            fast = fast.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        temp = slow.next.next if slow.next else None
        slow.next = temp

        return dummy_head.next