class Solution:
    """Solution for rotating an array to the right by k steps.

    Given an integer array `nums`, rotate the array to the right by `k` steps,
    where `k` is non-negative. The rotation should be done in-place, modifying
    the input array directly.
    """

    def rotate(self, nums: list[int], k: int) -> None:
        """Rotates the array to the right by k steps in-place.

        Args:
            nums (list[int]): List of integers.
            k (int): Number of steps to rotate.

        Returns:
            None: Modifies nums in-place.
        """
        k = k % len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])