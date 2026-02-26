import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """
        Given the root of a binary tree, return its level order
        traversal (breadth-first traversal) as a list of lists of
        node values.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            List[List[int]]: A list where each sublist contains
                values of nodes at the same depth level.
        """
        if not root:
            return []
        res = []
        q = collections.deque([(root, 0)])
        while q:
            n, depth = q.popleft()
            if depth == len(res):
                res.append([])
            res[-1].append(n.val)
            if n.left:
                q.append((n.left, depth + 1))
            if n.right:
                q.append((n.right, depth + 1))

        return res
