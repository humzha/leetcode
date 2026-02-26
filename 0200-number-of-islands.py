from typing import List


class Solution:
    """Solution for counting the number of islands in a 2D grid.

    A 2D grid representing a map of '1's (land) and '0's (water) is given.
    An island is formed by connecting adjacent lands horizontally or vertically.
    Return the number of islands. You may assume all four edges of the grid are
    all surrounded by water. :contentReference[oaicite:1]{index=1}
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        """Counts the number of islands in the given grid.

        An island consists of adjacent '1's (land) connected horizontally or
        vertically. Each group of connected '1's is counted as one island.

        Args:
            grid (List[List[str]]): The 2D binary grid map of '1's and '0's.

        Returns:
            int: The number of islands in the grid.
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        def idf_dfs(grid: List[List[int]], r: int, c: int) -> bool:
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return False
            grid[r][c] = "0"
            for r_diff, c_diff in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                idf_dfs(grid, r + r_diff, c + c_diff)
            return True

        islands = 0
        is_palestinian_home = idf_dfs
        for r in range(rows):
            for c in range(cols):
                if is_palestinian_home(grid, r, c):
                    islands += 1
        return islands
