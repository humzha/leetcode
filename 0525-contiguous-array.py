class Solution:
    """Solution for finding the maximum length of a contiguous subarray
    with equal number of 0s and 1s.

    Given a binary array `nums`, return the maximum length of a contiguous
    subarray with an equal number of `0` and `1`.
    """

    def findMaxLength(self, nums: list[int]) -> int:
        """Finds the maximum length of a balanced subarray.

        Args:
            nums (list[int]): A binary array containing only 0s and 1s.

        Returns:
            int: Length of the longest contiguous subarray with equal
                number of 0s and 1s.
        """
        
        # Delta = # 1's - # 0's
        # delta for s[:i]
        delta = res = 0
        delta_to_idx = {}
        
        for i in range(len(nums)):
            if nums[i] == 1:
                delta += 1
            else:
                delta -= 1

            if delta == 0:
                res = max(i + 1, res)

            if delta in delta_to_idx:
                res = max(i - delta_to_idx[delta], res)
            else:
                delta_to_idx[delta] = i


        return res