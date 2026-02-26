class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Given a sorted array of integers nums and an integer target,
        search for target in nums. If found, return its index.
        Otherwise, return -1.
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target < nums[m]:
                r = m - 1
            elif target == nums[m]:
                return m
            else:
                l = m + 1
        return -1
