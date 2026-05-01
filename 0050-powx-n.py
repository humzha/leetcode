class Solution:
    """Solution for computing x raised to the power n (x^n).

    Given a floating-point number x and an integer n, return x^n.

    Constraints include handling:
    - Positive powers
    - Negative powers
    - Large exponents efficiently
    """

    def myPow(self, x: float, n: int) -> float:
        """Computes x raised to power n.

        Args:
            x (float): Base value.
            n (int): Exponent value.

        Returns:
            float: Result of x^n.
        """
        def f(x: float, n: int) -> float:
            # n is guaranteed to be positive
            if n == 0:
                return 1
            elif n == 1:
                return x
            if n % 2 == 1:
                return f(x, n - 1) * x
            return f(x * x, n // 2)

        if n < 0:
            return 1 / f(x, abs(n))
        return f(x, n)