class Solution:
    """Solution for finding the minimal length subarray sum >= target.

    Given an array of positive integers nums and a positive integer target,
    return the minimal length of a contiguous subarray whose sum is greater
    than or equal to target. If no such subarray exists, return 0.
    """

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = curr_sum = 0
        min_len = float('inf')
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                curr_sum -= nums[l]
                min_len = min(r - l + 1, min_len)
                l += 1
                
        if min_len == float('inf'):
            return 0
        return min_len