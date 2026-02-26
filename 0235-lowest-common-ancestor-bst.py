# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # In a BST, starting from the top
        # A node is the LCA of two nodes if p, q cannot both go into either subtree left/right
        # If they can the LCA of p/q exists in that node

        # Assumptions:
        # p/q exist in the tree

        def lca(root: TreeNode) -> TreeNode:
            if p.val < root.val and q.val < root.val:
                return lca(root.left)
            elif p.val > root.val and q.val > root.val:
                return lca(root.right)
            return root

        return lca(root)
