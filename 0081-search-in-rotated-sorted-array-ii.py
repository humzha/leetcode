class Solution:
    """Solution for searching a target in a rotated sorted array with duplicates.

    Given an integer array nums sorted in non-decreasing order (not necessarily
    with distinct values) and rotated at an unknown pivot, return true if target
    is in nums, false otherwise. Must minimize overall operation steps as much
    as possible.
    """

    def search(self, nums: list[int], target: int) -> bool:
        # Yooour implementation here
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif nums[l] == nums[m]:
                l += 1
            # 4 5 6 1 2 3 , target = 5
            # L...M is sorted
            elif nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[l] > nums[m]:
            # 4 5 1 2 3 , target = 2
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False