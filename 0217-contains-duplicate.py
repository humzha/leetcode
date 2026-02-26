class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, determine if any value appears
        at least twice in the array. Return True if any value is
        duplicated, otherwise False.

        Args:
            nums (List[int]): The input array of integers.

        Returns:
            bool: True if any element appears more than once, False otherwise.
        """
        return len(set(nums)) != len(nums)
