from collections import deque

class Solution:
    """Solution for finding the shortest path from the starting position to any food cell in a grid.

    You are given an m x n grid where:
    - '*' represents your starting position (exactly one)
    - '#' represents food (one or more)
    - 'O' represents open space
    - 'X' represents obstacles

    You can move up, down, left, or right. Return the minimum number of steps
    required to reach any food cell. Return -1 if it is not possible.
    """

    def getFood(self, grid: list[list[str]]) -> int:
        """Finds the shortest number of steps from '*' to any '#'.

        Args:
            grid (list[list[str]]): 2D grid of characters representing the map.

        Returns:
            int: Minimum number of steps to reach food, or -1 if unreachable.
        """

        rows, cols = len(grid), len(grid[0])
        # (r, c, dist)
        q = deque()

        # Add starting position to the BFS queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '*':
                    q.append((r, c, 0))
        
        FOOD = '#'
        OPEN = 'O'
        OBSTACLE = 'X'

        while q:
            r, c, distance = q.popleft()       
            for rc, cd in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                rn, cn = r + rc, c + cd
                if (rn < 0 or rn >= rows) or (cn < 0 or cn >= cols):
                    continue
                if grid[rn][cn] == FOOD:
                    return distance + 1
                elif grid[rn][cn] == OPEN:
                    grid[rn][cn] = OBSTACLE
                    q.append((rn, cn, distance + 1))

        return -1