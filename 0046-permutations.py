from typing import List


class Solution:
    """Solution for returning all possible permutations of a list of distinct integers.

    Given an array `nums` of distinct integers, return all possible permutations.
    You may return the answer in any order. This function produces every unique
    arrangement of the elements of `nums`.:contentReference[oaicite:0]{index=0}
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        """Generates all possible permutations of the input list.

        Args:
            nums (List[int]): A list of distinct integers.

        Returns:
            List[List[int]]: A list of lists, where each inner list is a unique
                permutation of the input.
        """
        res = []

        def dfs(nums: List[int], path: List[int]):
            if not nums:
                res.append(path.copy())
            for i, n in enumerate(nums):
                dfs(
                    nums[:i] + nums[i + 1 :],
                    path + [n],
                )

        dfs(nums, [])
        return res
