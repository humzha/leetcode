class Solution:
    """Solution for setting matrix rows and columns to zero in-place.

    Given an m x n matrix, if an element is 0, set its entire row and column
    to 0. You must modify the matrix in-place.
    """

    def setZeroes(self, matrix: list[list[int]]) -> None:
        """Modifies the matrix in-place.

        Args:
            matrix (list[list[int]]): 2D matrix.

        Returns:
            None
        """
        # We can use the 0th row and the 0th col as storage space
        # [0][0] belongs to both the 0th row and col
        # [0][0] represents if 0th row should be 0'd
        # zero_col0 represents if 0th col should be 0'd
        
        # 0th row is storage space for cols
        
        rows, cols = len(matrix), len(matrix[0])
        zero_col0 = False
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        zero_col0 = True
                    else:
                        matrix[0][j] = 0

        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0
        
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0
        if zero_col0:
            for i in range(rows):
                matrix[i][0] = 0
