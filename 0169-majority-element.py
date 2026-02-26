class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Given an array of size n, return the majority element.
        The majority element is the element that appears more than
        ⌊n / 2⌋ times. You may assume that the array is non-empty
        and the majority element always exists.

        Args:
            nums (List[int]): The input array of integers.

        Returns:
            int: The element that appears more than n/2 times.
        """
        count = res = 0
        for n in nums:
            # Unset
            if count == 0:
                count = 0
                res = n
            elif res == n:
                count += 1
            else:
                count -= 1
        return res
