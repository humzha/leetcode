from typing import List


class Solution:
    """Solution for returning all elements of a matrix in spiral order.

    Given an `m x n` matrix, return all elements of the matrix in spiral
    order, starting from the top-left corner and moving right, then down,
    then left, then up, and continuing inward in a spiral pattern.
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Returns the elements of the matrix in spiral order.

        Args:
            matrix (List[List[int]]): The 2D list of integers.

        Returns:
            List[int]: A list of all elements in the matrix, traversed in
                spiral order.
        """
        rows, cols = len(matrix), len(matrix[0])
        row_start, row_end = 0, rows - 1
        col_start, col_end = 0, cols - 1
        RIGHT, DOWN, LEFT, UP = range(4)
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        res = []
        r = c = state = 0
        for _ in range(rows * cols):
            res.append(matrix[r][c])

            # Change direction if at the end
            dr, dc = DIRECTIONS[state]
            nr, nc = r + dr, c + dc

            if state == RIGHT and nc > col_end:
                col_end = c - 1
                state = (state + 1) % 4
                if (r, nc) == (0, cols):
                    row_start += 1
            elif state == DOWN and nr > row_end:
                row_end = r - 1
                state = (state + 1) % 4
            elif state == LEFT and nc < col_start:
                col_start = c + 1
                state = (state + 1) % 4
            elif state == UP and nr < row_start:
                row_start = r + 1
                state = (state + 1) % 4

            dr, dc = DIRECTIONS[state]
            r, c = r + dr, c + dc

        return res
