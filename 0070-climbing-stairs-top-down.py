class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Given n steps to reach the top of a staircase, where each
        move allows climbing either 1 or 2 steps, return the number
        of distinct ways to reach the top.

        Args:
            n (int): The total number of steps in the staircase.

        Returns:
            int: The number of distinct ways to reach the top.
        """
        dp = [1 if i <= 1 else None for i in range(n + 1)]

        def climb_stairs(i: int) -> int:
            # OOB
            if i >= len(dp):
                raise ValueError("Amount greater than allocated for dp array")
            # Compute
            if dp[i] is None:
                dp[i] = climb_stairs(i - 1) + climb_stairs(i - 2)
            return dp[i]

        return climb_stairs(n)
