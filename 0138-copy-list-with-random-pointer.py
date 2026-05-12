# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    """Solution for deep copying a linked list with random pointers.

    Given a linked list where each node contains an additional random pointer
    to any node or null, construct and return a deep copy of the list.
    
    The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
    """

    def copyRandomList(self, head: 'Node') -> 'Node':
        # Your implementation here
        curr = head
        mp = {}
        while curr:
            mp[curr] = Node(curr.val, next=curr.next, random=curr.random)
            curr = curr.next
            
        curr = head
        while curr:
            temp = curr.next
            mp[curr].next = mp.get(curr.next)
            mp[curr].random = mp.get(curr.random)
            curr = temp
        
        return mp.get(head)