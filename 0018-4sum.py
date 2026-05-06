class Solution:
    """Solution for finding all unique quadruplets that sum to a target.

    Given an array nums of n integers, return all unique quadruplets
    [nums[a], nums[b], nums[c], nums[d]] such that:
    0 <= a, b, c, d < n and a, b, c, d are distinct,
    and nums[a] + nums[b] + nums[c] + nums[d] == target.
    """

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # Your implementation here
        nums.sort()
        res, quad = [], []
        def k_sum(k: int, start: int, target: int):
            if k > 2:
                for i in range(start, len(nums) - k + 1):
                    # Avoid dupes
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    k_sum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            # k == 2:
            l, r = start, len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        k_sum(4, 0, target)
        return res