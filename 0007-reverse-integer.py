class Solution:
    """Solution for reversing a 32-bit signed integer.

    Given a signed 32-bit integer `x`, return `x` with its digits reversed.
    If reversing causes the value to go outside the signed 32-bit integer
    range [-2^31, 2^31 - 1], return 0.
    """

    def reverse(self, x: int) -> int:
        """Reverses the digits of an integer with overflow handling.

        Args:
            x (int): Input integer.

        Returns:
            int: Reversed integer or 0 if overflow occurs.
        """
        neg = x < 0
        x = abs(x)
        res = 0
        while x:
            res = (res * 10) + x % 10
            x //= 10

        res = res * -1 if neg else res
        if res < -2 ** 31 or res > 2 ** 31 - 1:
            return 0
        return res