from collections import defaultdict

class Solution:
    """Solution for counting subarrays whose sum equals k.

    Given an integer array `nums` and an integer `k`, return the total number
    of contiguous subarrays whose sum equals `k`.
    """

    def subarraySum(self, nums: list[int], k: int) -> int:
        """Counts the number of subarrays with sum equal to k.

        Args:
            nums (list[int]): List of integers (can be positive, zero, or negative).
            k (int): Target sum.

        Returns:
            int: Number of subarrays whose sum equals k.
        """
        acc_sum = res = 0
        # prefix_sum -> number of subarrays that this added to subarrays of s[:i]
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        for i in range(len(nums)):
            acc_sum += nums[i]
            # p + k = acc_sum
            p = acc_sum - k
            if p in prefix_sums:
                res += prefix_sums[p]
            prefix_sums[acc_sum] += 1
        return res