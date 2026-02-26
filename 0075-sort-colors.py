from typing import List


class Solution:
    """Solution for sorting an array with three distinct values in linear time.

    Given an array `nums` with n objects colored 0, 1, or 2, sort them in place
    so that objects of the same color are adjacent, with the colors in the order
    0, 1, and 2. You must solve this problem without using the library’s
    sort function.
    """

    def sortColors(self, nums: List[int]) -> None:
        """Sorts the list of colors in place.

        Args:
            nums (List[int]): The list of integers representing colors 0, 1, and 2.

        Returns:
            None: Modifies `nums` in place to be ordered 0 → 1 → 2.
        """
        RED, WHITE, BLUE = range(3)
        n = len(nums)
        j = 0

        for i in range(n):
            if nums[i] == RED:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

        j = n - 1
        for i in range(n - 1, -1, -1):
            if nums[i] == BLUE:
                nums[j], nums[i] = nums[i], nums[j]
                j -= 1
