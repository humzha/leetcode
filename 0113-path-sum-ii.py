class Solution:
    """Solution for finding all root-to-leaf paths with a given sum.

    Given the root of a binary tree and an integer targetSum, return all root-to-leaf
    paths where the sum of the node values in the path equals targetSum.
    """

    def pathSum(self, root: 'TreeNode', targetSum: int) -> list[list[int]]:
        """Finds all valid root-to-leaf paths with sum equal to targetSum.

        Args:
            root (TreeNode): Root of the binary tree.
            targetSum (int): Target sum to match.

        Returns:
            list[list[int]]: List of valid root-to-leaf paths.
        """
        # numbers can be negative, cant prune

        res = []
        # Pre order traverse all root to leaf paths, backtracking
        def dfs(n: 'TreeNode', curr_sum: int, path: list[int]):
            if not n:
                return

            curr_sum += n.val
            path.append(n.val)

            if not n.left and not n.right and curr_sum == targetSum:
                res.append(path.copy())

            dfs(n.left, curr_sum, path)
            dfs(n.right, curr_sum, path)

            path.pop()

        dfs(root, 0, [])
        return res