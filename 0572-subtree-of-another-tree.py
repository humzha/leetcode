class Solution:
    def isSubtree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode],
    ) -> bool:
        """
        Given the roots of two binary trees root and subRoot,
        determine whether subRoot is a subtree of root. A subtree
        of a tree consists of a node in the tree and all of its
        descendants, and must match in structure and node values.

        Args:
            root (Optional[TreeNode]): The root of the main tree.
            subRoot (Optional[TreeNode]): The root of the subtree.

        Returns:
            bool: True if subRoot is a subtree of root, False otherwise.
        """

        def is_same(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a and not b:
                return True
            if bool(a) ^ bool(b):
                return False
            return (
                a.val == b.val and is_same(a.left, b.left) and is_same(a.right, b.right)
            )

        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        return (
            is_same(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
