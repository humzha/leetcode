class Solution:
    """Solution for finding the first missing positive integer.

    Given an unsorted integer array nums, return the smallest positive
    integer that is not present in nums. Must run in O(n) time and O(1) space.
    """

    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = (len(nums) + 2)

        for i in range(len(nums)):
            mapped_idx = abs(nums[i]) - 1
            if mapped_idx < len(nums) and nums[mapped_idx] > 0:
                nums[mapped_idx] *= -1

        for i in range(1, len(nums) + 1):
            mapped_idx = i - 1
            if nums[mapped_idx] > 0:
                return i

        # [1, 2, 3], len = 3
        # [1..n +1]
        # 
        return len(nums) + 1
    
print(Solution().firstMissingPositive([3, 1]))
print(Solution().firstMissingPositive([0, 1, 2]))