class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return the length of its
        diameter. The diameter is the length of the longest path
        between any two nodes in the tree and may or may not pass
        through the root.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            int: The length of the diameter of the binary tree.
        """
        # None -> 0
        # Leaf -> 1
        #  1
        # 2 3
        # diam(2) -> 1
        # diam(3) -> 1
        # diam(1) -> 2, res = 2
        # diameter returns the longest paths length that terminates at the parent node
        # the result includes the path needed to connect it to the parent
        res = 0

        def diameter(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            dia_left = diameter(root.left)
            dia_right = diameter(root.right)
            res = max(res, dia_left + dia_right)
            return 1 + max(dia_left, dia_right)

        diameter(root)
        return res
