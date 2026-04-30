from collections import deque

class Solution:
    """Solution for binary tree zigzag level order traversal.

    Given the root of a binary tree, return the zigzag level order traversal
    of its nodes' values.

    Zigzag means:
    - Level 0: left → right
    - Level 1: right → left
    - Level 2: left → right
    - ... alternating each level
    """

    def zigzagLevelOrder(self, root: 'TreeNode') -> list[list[int]]:
        """Returns zigzag level order traversal of the binary tree.

        Args:
            root (TreeNode): Root of the binary tree.

        Returns:
            list[list[int]]: Node values level by level in zigzag order.
        """
        if not root:
            return []
        q = deque([(root, 0)])
        res = []

        while q:
            n, height = q.popleft()
            if height == len(res):
                res.append([])
            res[-1].append(n.val)
            if n.left:
                q.append((n.left, height + 1))
            if n.right:
                q.append((n.right, height + 1))

        for i in range(1, len(res), 2):
            res[i].reverse()

        return res