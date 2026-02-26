# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if bool(p) ^ bool(q):
                return False
            if not p and not q:
                return True
            return (
                p.val == q.val
                and is_same_tree(p.left, q.left)
                and is_same_tree(p.right, q.right)
            )

        return is_same_tree(p, q)
