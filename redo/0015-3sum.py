class Solution:
    """Solution for finding all unique triplets that sum to zero.

    Given an integer array nums, return all triplets [nums[i], nums[j], nums[k]]
    such that i != j, i != k, j != k and nums[i] + nums[j] + nums[k] == 0.
    The solution set must not contain duplicate triplets.
    """

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Your implementation here
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r] + nums[i]
                if curr_sum < 0:
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    res.append((nums[l], nums[r], nums[i]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r-= 1
        return res