class Solution:
    """Solution for determining if you can reach the last index of an array.

    You are given an integer array `nums`. You are initially positioned at the
    first index, and each element represents your maximum jump length at that
    position.

    Return True if you can reach the last index, or False otherwise.
    """

    def canJump(self, nums: list[int]) -> bool:
        """Checks whether the last index is reachable from the first index.

        Args:
            nums (list[int]): A list of non-negative integers representing
                maximum jump lengths.

        Returns:
            bool: True if the last index can be reached, otherwise False.
        """
        farthest_can_go = 0
        i = 0
        while i <= farthest_can_go and i < len(nums):
            farthest_can_go = max(farthest_can_go, nums[i] + i)
            i += 1
        return farthest_can_go >= len(nums) - 1