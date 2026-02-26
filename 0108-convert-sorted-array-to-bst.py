class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        """
        Given a sorted array of integers, convert it into a height-balanced
        binary search tree (BST). A height-balanced BST is one where the
        depth of the two subtrees of every node never differs by more than one.

        Args:
            nums (List[int]): A sorted array of integers.

        Returns:
            Optional[TreeNode]: The root of the height-balanced BST.
        """

        def create_bst(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            elif l == r:
                return TreeNode(nums[l])
            m = (l + r) // 2
            node = TreeNode(nums[m])
            node.left = create_bst(l, m - 1)
            node.right = create_bst(m + 1, r)
            return node

        return create_bst(0, len(nums) - 1)
