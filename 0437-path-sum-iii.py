class Solution:
    """Solution for counting paths in a binary tree that sum to a target.

    Given the root of a binary tree and an integer targetSum, return the number
    of paths where the sum of the values along the path equals targetSum.

    A path:
    - Does NOT need to start at the root
    - Does NOT need to end at a leaf
    - MUST go downward (parent → child)
    """

    def pathSum(self, root: 'TreeNode', targetSum: int) -> int:
        """Counts the number of valid paths.

        Args:
            root (TreeNode): Root of the binary tree.
            targetSum (int): Target sum.

        Returns:
            int: Number of paths whose sum equals targetSum.
        """
        # Brute Force
        def calc_ps(root: 'TreeNode', path_sum) -> int:
            """
            Return all number of path whose sum equal targetSum
            where it is rooted at the initial root calc_ps is called on
            """
            if not root:
                return 0
            curr_ps = root.val + path_sum
            return (1 if curr_ps == targetSum else 0) + calc_ps(root.left, curr_ps) + calc_ps(root.right, curr_ps)
            
        def dfs(root: 'TreeNode') -> int:
            if not root:
                return 0
            res = 0
            res += calc_ps(root, 0)
            res += dfs(root.left) + dfs(root.right)
            return res
        return dfs(root)