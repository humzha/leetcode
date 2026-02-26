from typing import Optional
from dataclasses import dataclass


@dataclass
class Result:
    """Return value for LCA recursive helper.

    Tracks the lowest common ancestor candidate and count of targets found
    in a subtree. When found == 2, node contains the LCA.
    lca(root, p, q) -> State(LCA, 2)

    Attributes:
        node: The LCA candidate if both p and q are found in this subtree,
            otherwise None.
        found: Number of target nodes (p and/or q) found in this subtree.
            Value is 0, 1, or 2.
    """

    node: Optional["TreeNode"]
    found: int


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """Solution for finding the lowest common ancestor (LCA) of two nodes in a binary tree.

    Given a binary tree and two nodes `p` and `q` that exist in the tree, return the
    lowest common ancestor (LCA) of `p` and `q`. The lowest common ancestor is
    defined as the lowest node in the tree that has both `p` and `q` as descendants
    (a node can be a descendant of itself). :contentReference[oaicite:0]{index=0}
    """

    def lowestCommonAncestor(
        self,
        root: Optional["TreeNode"],
        p: "TreeNode",
        q: "TreeNode",
    ) -> Optional["TreeNode"]:
        """Finds the lowest common ancestor of two nodes in a binary tree.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.
            p (TreeNode): First target node.
            q (TreeNode): Second target node.

        Returns:
            Optional[TreeNode]: The lowest common ancestor node if found; otherwise
                None.
        """

        def lca(
            curr_node: Optional["TreeNode"], p: "TreeNode", q: "TreeNode"
        ) -> Result:
            if not curr_node:
                return Result(None, 0)

            left = lca(curr_node.left, p, q)
            if left.found == 2:
                return left

            right = lca(curr_node.right, p, q)
            if right.found == 2:
                return right

            found = (
                (1 if curr_node is p or curr_node is q else 0)
                + left.found
                + right.found
            )
            return Result(curr_node if found == 2 else None, found)

        return lca(root, p, q).node
