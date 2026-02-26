# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Given the root of a binary tree, invert the tree and return
        its root.
        """

        def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root:
                return None
            root.left, root.right = invert_tree(root.right), invert_tree(root.left)
            return root

        return invert_tree(root)
