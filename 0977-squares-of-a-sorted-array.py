class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """
        Given a sorted array of integers nums, return an array
        of the squares of each number sorted in non-decreasing
        order.

        Args:
            nums (List[int]): A sorted array of integers.

        Returns:
            List[int]: A sorted array of the squares of nums.
        """
        l, r = 0, len(nums) - 1
        res = []
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res.append(nums[l] ** 2)
                l += 1
            else:
                res.append(nums[r] ** 2)
                r -= 1
        return list(reversed(res))
