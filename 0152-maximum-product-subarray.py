class Solution:
    """Solution for finding the contiguous subarray with the largest product.

    Given an integer array `nums`, find a contiguous non-empty subarray within
    the array that has the largest product, and return the product.
    """

    def maxProduct(self, nums: list[int]) -> int:
        """Calculates the maximum product of a contiguous subarray.

        Args:
            nums (list[int]): A list of integers that may include negative values
                and zeros.

        Returns:
            int: The maximum product of any contiguous subarray.
        """
        if not nums:
            return -1

        res = mps_prev_pos = mps_prev_neg = nums[0]
        for n in nums[1:]:
            mps_pos = max(mps_prev_neg * n, mps_prev_pos * n, n)
            mps_neg = min(mps_prev_neg * n, mps_prev_pos * n, n)
            res = max(mps_pos, res)
            mps_prev_neg, mps_prev_pos = mps_neg, mps_pos
            
        return res