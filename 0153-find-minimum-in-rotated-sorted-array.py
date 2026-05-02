class Solution:
    """Solution for finding the minimum element in a rotated sorted array.

    Given a sorted array of unique elements that has been rotated between
    1 and n times, return the minimum element in O(log n) time.
    """

    def findMin(self, nums: list[int]) -> int:
        # Your implementation here
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        return nums[l]