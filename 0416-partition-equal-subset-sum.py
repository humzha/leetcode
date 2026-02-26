from typing import List


class Solution:
    """Solution for determining if a list can be partitioned into two subsets
    with equal sum.

    Given a **non-empty** array `nums` containing only **positive** integers,
    determine if the array can be partitioned into two subsets such that the
    sum of elements in both subsets is equal. ([leetcodee.com](https://leetcodee.com/problems/partition-equal-subset-sum/?utm_source=chatgpt.com))
    """

    def canPartition(self, nums: List[int]) -> bool:
        """Checks if the array can be split into two subsets with equal sum.

        Args:
            nums (List[int]): The list of positive integers.

        Returns:
            bool: True if such a partition exists; otherwise False.
        """
        sum_all = sum(nums)
        if sum_all % 2 == 1:
            return False
        target = sum_all // 2
        combination_sums = set([0])
        for i in range(len(nums) - 1, -1, -1):
            new_entries = set()
            for s in combination_sums:
                if s + nums[i] == target:
                    return True
                elif s + nums[i] < target:
                    new_entries.add(s + nums[i])
            combination_sums = combination_sums.union(new_entries)

        return False
