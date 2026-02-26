from typing import List, Deque, Tuple
from collections import deque


class Solution:
    """Solution for calculating the minimum time until all fresh oranges rot.

    You are given an m x n grid where each cell can have one of three values:
    - 0 representing an empty cell,
    - 1 representing a fresh orange,
    - 2 representing a rotten orange.

    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange
    becomes rotten. Return the minimum number of minutes that must elapse until no cell
    has a fresh orange. If this is impossible, return -1.
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        """Determines the minimum number of minutes needed to rot all fresh oranges.

        Args:
            grid (List[List[int]]): A 2D grid representing fresh and rotten oranges.

        Returns:
            int: The minimum number of minutes until all fresh oranges have rotted,
                 or -1 if it is impossible.
        """
        if not grid or not grid[0]:
            return 0

        EMPTY, FRESH, ROT = range(3)
        rows, cols = len(grid), len(grid[0])

        # (r, c, minute_became_rot)
        rotten_oranges: Deque[Tuple[int, int, int]] = deque()
        fresh_oranges: int = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == ROT:
                    rotten_oranges.append((r, c, 0))
                elif grid[r][c] == FRESH:
                    fresh_oranges += 1

        res = 0
        while rotten_oranges:
            r, c, minutes_taken = rotten_oranges.popleft()
            res = max(res, minutes_taken)

            # Rot other oranges
            for r_diff, c_diff in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r_nei, c_nei = r + r_diff, c + c_diff
                if (
                    0 <= r_nei < rows
                    and 0 <= c_nei < cols
                    and grid[r_nei][c_nei] == FRESH
                ):
                    grid[r_nei][c_nei] = ROT
                    fresh_oranges -= 1
                    rotten_oranges.append((r_nei, c_nei, minutes_taken + 1))

        return res if fresh_oranges == 0 else -1
