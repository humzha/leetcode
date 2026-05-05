class Solution:
    """Solution for concatenating an array with itself.

    Given an integer array nums, return an array ans of length 2n
    where ans[i] == nums[i] for 0 <= i < n, and ans[i] == nums[i-n]
    for n <= i < 2n.
    """

    def getConcatenation(self, nums: list[int]) -> list[int]:
        # Your implementation here
        return nums + nums