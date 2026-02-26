class Solution:
    """Solution for counting unique paths in a grid.

    A robot is located at the top-left corner of an m x n grid. It can only
    move either down or right at any point in time. The robot is trying to
    reach the bottom-right corner of the grid. Return the number of possible
    unique paths from start to finish.
    """

    def uniquePaths(self, m: int, n: int) -> int:
        """Calculates the number of unique paths in an m x n grid.

        Args:
            m (int): Number of rows in the grid.
            n (int): Number of columns in the grid.

        Returns:
            int: The total unique paths from top-left to bottom-right.
        """
        dp = [
            [1 if i == m - 1 and j == n - 1 else None for j in range(n)]
            for i in range(m)
        ]

        def dfs(i: int, j: int) -> int:
            if i >= m or j >= n:
                return 0

            if dp[i][j] is None:
                dp[i][j] = 0
                dp[i][j] += dfs(i + 1, j)
                dp[i][j] += dfs(i, j + 1)
            return dp[i][j]

        return dfs(0, 0)
