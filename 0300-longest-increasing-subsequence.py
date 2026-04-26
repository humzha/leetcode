class Solution:
    """Solution for finding the length of the longest increasing subsequence.

    Given an integer array `nums`, return the length of the longest strictly
    increasing subsequence.
    """

    def lengthOfLIS(self, nums: list[int]) -> int:
        """Calculates the length of the longest increasing subsequence.

        Args:
            nums (list[int]): A list of integers.

        Returns:
            int: The length of the longest strictly increasing subsequence.
        """
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            # Look back at all prev LIS, and continue the longest one:
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)