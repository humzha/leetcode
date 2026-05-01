class Solution:
    """Solution for searching a value in a 2D matrix.

    You are given an m x n matrix with the following properties:
    - Each row is sorted in non-decreasing order.
    - The first integer of each row is greater than the last integer of the previous row.

    Return True if target exists in the matrix, otherwise False.
    """

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """Searches for target in the matrix.

        Args:
            matrix (list[list[int]]): 2D sorted matrix.
            target (int): Value to search for.

        Returns:
            bool: True if found, else False.
        """
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        # bisect left on the last column for the row
        # top = l, bot = r
        top, bot = 0, rows - 1
        while top < bot:
            mid_row_idx = (top + bot) // 2
            if target > matrix[mid_row_idx][-1]:
                top = mid_row_idx + 1
            else:
                bot = mid_row_idx
        if top > bot:
            return False

        # bot == top == row_to_search
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[top][m] == target:
                return True
            elif matrix[top][m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False
