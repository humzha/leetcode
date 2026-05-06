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
        prefix_sum_to_count = defaultdict(int)
        prefix_sum_to_count[0] = 1
        for n in nums:
            # prefix_sum + k = acc_sum
            # prefix_sum = acc_sum - k
            acc_sum += n
            if acc_sum - k in prefix_sum_to_count:
                res += prefix_sum_to_count[acc_sum - k]
            prefix_sum_to_count[acc_sum] += 1
        
        return res