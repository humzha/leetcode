from typing import Tuple


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        A height-balanced binary tree is one in which the depth of
        the two subtrees of every node never differs by more than one.
        """

        # We need to check for every node if their children are both
        # balanced
        # the depth of the node's subtree so that the parent node can compute its balancedness
        def is_balanced_height(root: Optional[TreeNode]) -> Tuple[bool, int]:
            # 3 cases
            # None
            # Leaf
            # Subtree with at least one non-null child
            if root is None:
                return (True, 0)
            if not root.left and not root.right:
                return (True, 1)
            lb, lh = is_balanced_height(root.left)
            rb, rh = is_balanced_height(root.right)
            return (lb and rb and abs(lh - rh) <= 1, max(lh, rh) + 1)

        return is_balanced_height(root)[0]
