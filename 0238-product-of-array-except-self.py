from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array answer such
        that answer[i] is the product of all the elements of nums
        except nums[i], without using division and in O(n) time.

        Args:
            nums (List[int]): An array of integers.

        Returns:
            List[int]: An array where each element is the product of
                all other elements in nums except the one at the same index.
        """
        # res [i] = product(nums[:i]) * product(nums[i + 1:])
        res = [1 for _ in range(len(nums))]

        # Left pass and multiply every number in the res array
        left_product = 1
        for i, n in enumerate(nums):
            res[i] *= left_product
            left_product *= n

        right_product = 1
        # Technically uses O(n) space, can change to while
        for i, n in reversed(list(enumerate(nums))):
            res[i] *= right_product
            right_product *= n
        return res
