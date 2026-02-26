class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """
        Given an array nums containing n distinct numbers in the
        range [0, n], return the only number in the range that
        is missing from the array.

        Args:
            nums (List[int]): An array of n distinct numbers in [0, n].

        Returns:
            int: The missing number from the array.
        """
        n = len(nums) + 1
        res = 0
        for i in range(n):
            res ^= i
        for n in nums:
            res ^= n
        return res
