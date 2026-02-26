class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Given a non-empty array of integers where every element
        appears twice except for one, return the element that
        appears only once.

        Args:
            nums (List[int]): The input array of integers.

        Returns:
            int: The single number that appears only once.
        """
        res = 0
        for n in nums:
            res ^= n
        return res
