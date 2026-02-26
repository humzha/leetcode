from typing import List


class Solution:
    """Solution for rotating an n x n matrix (image) by 90 degrees clockwise.

    You are given an n x n 2D matrix representing an image. Rotate the image
    by 90 degrees (clockwise) in place, modifying the input 2D matrix directly
    without allocating another matrix.([turn0search0])
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """Rotates the input matrix by 90 degrees clockwise.

        Args:
            matrix (List[List[int]]): A square 2D list of integers.

        Returns:
            None: Modifies `matrix` in place.
        """
        n = len(matrix)

        # 5 -> 2, 6 -> 3
        borders = n // 2
        for b in range(borders):
            for i in range(b, n - b - 1):
                flip_i = n - i - 1
                row_a, col_a = (b, i)
                row_b, col_b = (i, n - 1 - b)  # 5
                row_c, col_c = (n - b - 1, flip_i)
                row_d, col_d = (flip_i, b)
                (
                    matrix[row_a][col_a],
                    matrix[row_b][col_b],
                    matrix[row_c][col_c],
                    matrix[row_d][col_d],
                ) = (
                    matrix[row_d][col_d],
                    matrix[row_a][col_a],
                    matrix[row_b][col_b],
                    matrix[row_c][col_c],
                )
