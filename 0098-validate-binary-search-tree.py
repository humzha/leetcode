from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """Solution for validating if a binary tree is a valid Binary Search Tree (BST)."""

    def isValidBST(self, root: Optional["TreeNode"]) -> bool:
        """Determines if the given binary tree is a valid BST.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            bool: True if the tree is a valid BST, False otherwise.
        A valid BST (Binary Search Tree) is defined as follows:

        - The left subtree of a node contains only nodes with keys strictly less than the node's key.
        - The right subtree of a node contains only nodes with keys strictly greater than the node's key.
        - Both the left and right subtrees must also be binary search trees.
        """

        def is_valid(
            root: Optional["TreeNode"],
            left_bound: int | float,
            right_bound: int | float,
        ) -> bool:
            if not root:
                return True
            if root.val <= left_bound or root.val >= right_bound:
                return False
            return is_valid(root.left, left_bound, root.val) and is_valid(
                root.right, root.val, right_bound
            )

        return is_valid(root, float("-inf"), float("inf"))
