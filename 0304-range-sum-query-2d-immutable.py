class NumMatrix:
    """2D prefix sum data structure for O(1) range sum queries.

    Initializes with a 2D integer matrix and supports sumRegion queries
    that return the sum of elements within a specified rectangular region.
    """

    def __init__(self, matrix: list[list[int]]):
        # Your implementation here
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.prefix_sum = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            curr_row_sum = 0
            for j in range(self.cols):
                curr_row_sum += matrix[i][j]
                self.prefix_sum[i][j] = curr_row_sum + (self.prefix_sum[i - 1][j] if i - 1 >= 0 else 0)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        tl_x, tl_y = row1 - 1, col1 - 1
        tr_x, tr_y = row1 - 1, col2
        bl_x, bl_y = row2, col1 - 1
        
        TL = self.prefix_sum[tl_x][tl_y] if tl_x >= 0 and tl_y >= 0 else 0
        TR = self.prefix_sum[tr_x][tr_y] if tr_x >= 0 and tr_y >= 0 else 0
        BL = self.prefix_sum[bl_x][bl_y] if bl_x >= 0 and bl_y >= 0 else 0
        return self.prefix_sum[row2][col2] - (TR + (BL - TL))