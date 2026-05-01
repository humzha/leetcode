from collections import defaultdict

class Solution:
    """Solution for counting paths in a binary tree that sum to a target.

    Given the root of a binary tree and an integer target_sum, return the number
    of paths where the sum of the values along the path equals target_sum.

    A path:
    - Does NOT need to start at the root
    - Does NOT need to end at a leaf
    - MUST go downward (parent → child)
    """

    def pathSum(self, root: 'TreeNode', target_sum: int) -> int:
        """Counts the number of valid paths.

        Args:
            root (TreeNode): Root of the binary tree.
            target_sum (int): Target sum.

        Returns:
            int: Number of paths whose sum equals target_sum.
        """
        def backtrack(root: 'TreeNode', prefix_sum: dict[int, int], running_sum: int) -> int:
            if not root:
                return 0

            running_sum += root.val

            # running_sum = path_sum from the initial node
            # p = path_sum from the initial node to any parent_above (prefix_sh)
            # running_sum = target_sum + p
            # p = running_sum - target_sum
            res = 0
            if running_sum - target_sum in prefix_sum:
                res += prefix_sum[running_sum - target_sum]

            prefix_sum[running_sum] += 1
            res += backtrack(root.left, prefix_sum, running_sum)
            res += backtrack(root.right, prefix_sum, running_sum)
            prefix_sum[running_sum] -= 1

            if prefix_sum[running_sum] == 0:
                del prefix_sum[running_sum]
            return res
            
        mp = defaultdict(int)
        mp[0] = 1
        return backtrack(root, mp, 0)