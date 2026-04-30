class Solution:
    """Solution for finding the largest square containing only 1's.

    Given an m x n binary matrix filled with '0's and '1's, return the area
    of the largest square containing only '1's.
    """

    def maximalSquare(self, matrix: list[list[str]]) -> int:
        """Finds the area of the largest square of '1's.

        Args:
            matrix (list[list[str]]): 2D binary matrix.

        Returns:
            int: Area of the largest square containing only '1's.
        """
        rows, cols = len(matrix), len(matrix[0])
        dp = [[None for _ in range(cols)] for _ in range(rows)]

        def max_square(i: int, j: int) -> int:
            if i >= rows or j >= cols:
                return -1
            elif dp[i][j] is None:
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    candidates = (max_square(i, j + 1),
                                  max_square(i + 1, j),
                                  max_square(i + 1, j + 1))
                    if all([c >= 1 for c in candidates]):
                        dp[i][j] = 1 + min(candidates)
                    else:
                        dp[i][j] = 1
            return dp[i][j]
            
        res = 0
        for i in range(rows):
            for j in range(cols):
                max_square(i, j)
                if dp[i][j]:
                    res = max(dp[i][j], res)
                
        return res ** 2