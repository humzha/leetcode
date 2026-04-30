from collections import deque

class Solution:
    """Solution for finding the minimum number of knight moves on an infinite chessboard.

    You are given a knight starting at coordinate (0, 0) on an infinite grid.
    Return the minimum number of moves required to reach a target position (x, y).

    A knight moves in an L-shape:
    - (±2, ±1)
    - (±1, ±2)
    """

    def minKnightMoves(self, x: int, y: int) -> int:
        """Computes the minimum number of knight moves to reach (x, y).

        Args:
            x (int): Target x-coordinate.
            y (int): Target y-coordinate.

        Returns:
            int: Minimum number of moves required.
        """
        # BFS to (x, y)
        # edges are valid knight moves
        # (x, y, moves)
        q = deque([(0, 0, 0)])
        visited = set([(0, 0)])
        while True:
            curr_x, curr_y, turn = q.popleft()
            if curr_x == x and curr_y == y:
                return turn

            # could squash the two together but cba
            for xd, yd in ((-2, -1), (2, -1), (-2, 1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)):
                nei_x = curr_x + xd
                nei_y = curr_y + yd
                if (nei_x, nei_y) in visited:
                    continue
                q.append((nei_x, nei_y, turn + 1))
                visited.add((nei_x, nei_y))