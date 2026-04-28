from collections import deque

class Solution:
    """Solution for finding the maximum width of a binary tree.

    Given the root of a binary tree, return the maximum width among all levels.

    The width of a level is defined as the number of positions between the
    leftmost and rightmost non-null nodes at that level, including null gaps
    as if the tree were a complete binary tree.
    """

    def widthOfBinaryTree(self, root: 'TreeNode') -> int:
        """Computes the maximum width of the binary tree.

        Args:
            root (TreeNode): Root of the binary tree.

        Returns:
            int: Maximum width across all levels.
        """
        # Level Order Traversal
        # # node, idx, height
        q = deque([(root, 0, 0)])
        prev_height = -1
        l = r = 0
        res = 0 
        while q:
            n, idx, height = q.popleft()
            if height > prev_height:
                l = r = idx
                prev_height = height
            l = min(l, idx)
            r = max(r, idx)
            res = max(r - l + 1, res)
            if n.left:
                q.append((n.left, idx * 2, height + 1))
            if n.right:
                q.append((n.right, idx * 2 + 1, height + 1))

        return res