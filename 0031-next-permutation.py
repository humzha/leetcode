class Solution:
    """Solution for rearranging the list into its next lexicographical permutation.

    Implement the next permutation of numbers in place, modifying the input list
    to the next greater permutation of numbers. If such arrangement is not
    possible, rearrange into the lowest (sorted in ascending) order. The
    replacement must be in place and use only constant extra memory.
    """

    def nextPermutation(self, nums: list[int]) -> None:
        """Transforms `nums` into the next lexicographical permutation.

        Args:
            nums (list[int]): A list of integers.

        Returns:
            None: Modifies `nums` in place.
        """
        if len(nums) < 2:
            return nums

        l = len(nums) - 1

        while l >= 0:
            if l == 0:
                nums.reverse()
                return
            # 3 2
            if nums[l - 1] < nums[l]:
                break
            l -= 1

        i = l - 1
        r = len(nums) - 1

        while nums[r] <= nums[i]:
            r -= 1

        nums[i], nums[r] = nums[r], nums[i]
        nums[l:] = sorted(nums[l:])