class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverse the bits of a given 32-bit unsigned integer.

        Args:
            n (int): A 32-bit unsigned integer.

        Returns:
            int: The integer resulting from reversing the bits of n.
        """

        def swap_bits(n: int, i: int, j: int) -> int:
            if i == j:
                return n
            if (n >> i) & 1 == (n >> j) & 1:
                return n
            return n ^ ((1 << i) | (1 << j))

        l, r = 0, 31
        while l < r:
            n = swap_bits(n, l, r)
            l += 1
            r -= 1
        return n
