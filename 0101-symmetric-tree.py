class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Given the root of a binary tree, check whether it is
        symmetric around its center (a mirror of itself).

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            bool: True if the tree is symmetric, False otherwise.
        """
        if not root:
            return True

        def is_symmetric(a: Optional[TreeNode], b: Optional[TreeNode]):
            if not a and not b:
                return True
            if bool(a) ^ bool(b):
                return False
            return (
                a.val == b.val
                and is_symmetric(a.left, b.right)
                and is_symmetric(a.right, b.left)
            )

        return is_symmetric(root.left, root.right)
