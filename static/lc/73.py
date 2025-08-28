class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        col_set_zero = False
        # Pick matrix[0][0] as the boolean for if matrix[0] (the row)
        # will be zeroed out
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    if j == 0:
                        col_set_zero = True
                    else:
                        matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0
        
        for i in range(rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0
        
        if col_set_zero:
            for i in range(rows):
                matrix[i][0] = 0