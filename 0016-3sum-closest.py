class Solution:
    """Solution for finding the 3Sum closest to a target.

    Given an integer array nums of length n and an integer target,
    find three integers at distinct indices whose sum is closest to target.
    Return the sum of the three integers.
    """

    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Your implementation here
        nums.sort()

        closest = float('-inf')
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                elif curr_sum == target:
                    return r
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1
        return closest