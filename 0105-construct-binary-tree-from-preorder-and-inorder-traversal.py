from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """Solution for constructing a binary tree from preorder and inorder traversal sequences.

    Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder
    traversal of a binary tree and `inorder` is the inorder traversal of the same tree,
    construct and return the binary tree. You may assume that there are no duplicate
    values in the tree. :contentReference[oaicite:0]{index=0}
    """

    def buildTree(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional["TreeNode"]:
        """Constructs the binary tree represented by the given traversals.

        Args:
            preorder (List[int]): The preorder traversal of the tree.
            inorder (List[int]): The inorder traversal of the tree.

        Returns:
            Optional[TreeNode]: The root of the constructed binary tree.
        """
        val_to_inorder_idx = {v: i for i, v in enumerate(inorder)}

        def build_tree(p: int, l: int, r: int) -> Optional["TreeNode"]:
            if p >= len(preorder) or l > r:
                return None
            node = TreeNode(preorder[p])

            # preorder
            # 0 1 2 3 4 5 6
            # A B C D E F G
            # p l l l r r r

            # inorder
            # l     m     r
            # 0 1 2 3 4 5 6
            # C B D A E F G
            # l l l m r r r
            inorder_idx = val_to_inorder_idx[node.val]
            left_size = inorder_idx - l

            node.left = build_tree(p + 1, l, inorder_idx - 1)
            node.right = build_tree(p + left_size + 1, inorder_idx + 1, r)

            return node

        return build_tree(0, 0, len(inorder))
