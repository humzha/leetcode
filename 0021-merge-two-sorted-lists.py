# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Docstring for mergeTwoLists

        :param self: Description
        :param list1: Description
        :type list1: Optional[ListNode]
        :param list2: Description
        :type list2: Optional[ListNode]
        :return: Description
        :rtype: Any
        You are given the heads of two sorted linked lists list1 and list2.

        Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

        Return the head of the merged linked list.
        """
        if not list1 and not list2:
            return None
        if bool(list1) ^ bool(list2):
            return list1 if list1 else list2
        dummy_head = tail = ListNode()
        while list1 or list2:
            list1_val = list1.val if list1 else float("inf")
            list2_val = list2.val if list2 else float("inf")
            if list1_val < list2_val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            tail.next = None
        return dummy_head.next
