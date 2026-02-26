from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """Solution for returning the values visible from the right side of a binary tree.

    Given the root of a binary tree, imagine yourself standing on the right side of it,
    and return the values of the nodes you can see ordered from top to bottom. A node
    is visible if it is the rightmost node at its depth level. :contentReference[oaicite:0]{index=0}
    """

    def rightSideView(self, root: Optional["TreeNode"]) -> List[int]:
        """Returns the list of node values visible when the tree is viewed from the right.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            List[int]: A list of integers representing the rightmost visible node at
                each level of the tree, from top (root) to bottom.
        """
        if not root:
            return []

        res = []
        q = deque([root])
        while q:
            level_size = len(q)
            for i in range(level_size):
                n = q.popleft()
                if i == level_size - 1:
                    res.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return res
