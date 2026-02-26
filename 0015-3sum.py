class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Given an integer array nums, return all unique triplets
        [a, b, c] such that a + b + c == 0. The solution set
        must not contain duplicate triplets.

        Args:
            nums (List[int]): The input array of integers.

        Returns:
            List[List[int]]: A list of unique triplets summing to zero.
        """

        """
        Solution set can't contain duplicate triplets
        """
        target = 0
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                curr_sum = nums[lo] + nums[hi] + nums[i]
                # 0 > -1
                if target > curr_sum:
                    lo += 1
                elif target < curr_sum:
                    hi -= 1
                else:
                    res.append((nums[i], nums[lo], nums[hi]))
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
        return res
