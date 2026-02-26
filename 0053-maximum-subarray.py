class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Given an integer array nums, find the contiguous subarray
        with the largest sum and return its sum.

        Args:
            nums (List[int]): An array of integers.

        Returns:
            int: The maximum sum of any contiguous subarray.
        """
        max_sum = prev_sum = nums[0]
        for i in range(1, len(nums)):
            # Largest sum of the contiguous subarray ending at nums[i]
            curr = max(nums[i], nums[i] + prev_sum)
            max_sum = max(max_sum, curr)

            prev_sum = curr
        return max_sum
