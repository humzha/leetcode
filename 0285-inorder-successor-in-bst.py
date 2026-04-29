class Solution:
    """Solution for finding the inorder successor of a node in a BST.

    Given the root of a binary search tree (BST) and a node `p`, return the
    inorder successor of that node in the BST. If the given node has no
    inorder successor, return None.

    The inorder successor of a node is the node with the smallest value
    greater than `p.val`.
    """

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """Finds the inorder successor of a given node in the BST.

        Args:
            root (TreeNode): Root of the binary search tree.
            p (TreeNode): Target node whose successor is to be found.

        Returns:
            TreeNode: The inorder successor node, or None if it does not exist.
        """
        # IOT
        if not root or not p:
            return None

        # In it's rightmost subtree
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        else:
            stack = []
            seen_p = False
            while root:
                stack.append(root)
                root = root.left
                
            while stack:
                n = stack.pop()
                if seen_p:
                    return n
                seen_p = n is p
                n = n.right
                while n:
                    stack.append(n)
                    n = n.left
        return None
    def inorderSuccessor_bst(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """Finds the inorder successor of a given node in the BST.

        Args:
            root (TreeNode): Root of the binary search tree.
            p (TreeNode): Target node whose successor is to be found.

        Returns:
            TreeNode: The inorder successor node, or None if it does not exist.
        """
        # IOT
        if not root or not p:
            return None

        res = None
        while root:
            if p.val < root.val:
                res = root
                root = root.left
            else:
                root = root.right
        return res