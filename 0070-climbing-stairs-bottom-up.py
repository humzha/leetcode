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
        # 012
        prev1, prev2 = 1, 1
        for _ in range(2, n + 1):
            curr = prev1 + prev2
            prev1, prev2 = curr, prev1
        return prev1
