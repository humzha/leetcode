class Solution:
    """Solution for finding the k-th smallest element in a Binary Search Tree (BST).

    Given the root of a BST and an integer `k`, return the k-th smallest
    value (1‑indexed) of all the values of the nodes in the tree.
    """

    def kthSmallest(self, root: 'TreeNode', k: int) -> int:
        """Returns the k-th smallest value in the BST.

        Args:
            root (TreeNode): The root of the binary search tree.
            k (int): The 1‑indexed order of the smallest element to retrieve.

        Returns:
            int: The k-th smallest value in the tree.
        """
        # In Order Traversal
        stack = []
        while root:
            stack.append(root)
            root = root.left
            
        res = None
        for _ in range(k):
            node = stack.pop()
            res = node
            node = node.right
            while node:
                stack.append(node)
                node = node.left

        return res.val