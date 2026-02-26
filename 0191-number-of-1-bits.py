class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Given an unsigned integer n, return the number of 1 bits
        in its binary representation (also known as the Hamming
        weight).

        Args:
            n (int): An unsigned integer.

        Returns:
            int: The number of 1 bits in n.
        """
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res
