class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Given an integer array nums, move all 0's to the end of the
        array while maintaining the relative order of the non-zero
        elements. The operation is performed in-place.

        Args:
            nums (List[int]): The input array of integers.

        Returns:
            None
        """

        """
        Write all the numbers to the back
        10204006
            1246
            
        Then write the numbers to the front
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        for i in range(j, len(nums)):
            nums[i] = 0
