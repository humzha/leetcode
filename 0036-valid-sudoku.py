class Solution:
    """Solution for validating whether a partially filled Sudoku board is valid.

    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to
    be validated according to the following rules:

    - Each row must contain the digits 1–9 without repetition.
    - Each column must contain the digits 1–9 without repetition.
    - Each of the nine 3 × 3 sub-boxes must contain the digits 1–9 without repetition.

    The Sudoku board may be partially filled, where empty cells are represented
    by the character '.'. A valid board does not necessarily mean the puzzle is solvable.
    """  # :contentReference[oaicite:0]{index=0}

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """Checks whether the given Sudoku board is valid.

        Args:
            board (list[list[str]]): A 9 × 9 grid containing digits '1'–'9'
                or '.' for empty cells.

        Returns:
            bool: True if the board satisfies Sudoku validity rules,
                otherwise False.
                
        
        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        """
        BOARD_LEN = 9
        # Row
        # Given a list, check if all numbers are either 1-9 or .
        # and that they are all unique
        def is_valid(arr: list[str]) -> bool:
            seen_nums = set()
            for c in arr:
                if c == '.':
                    continue
                elif c.isnumeric() and c != '0':
                    if c in seen_nums:
                        return False
                    seen_nums.add(c)
                else:
                    return False
            return True
        
        # Row
        for row in board:
            if not is_valid(row):
                return False

        # Col
        for col in range(BOARD_LEN):
            col_elems = []
            for row in range(BOARD_LEN):
                col_elems.append(board[row][col])
            if not is_valid(col_elems):
                return False
            
        for row_mult in range(3):
            for col_mult in range(3):
                row_start, col_start = 3 * row_mult, 3 * col_mult
                flattened_3x3 = []
                for rd in range(3):
                    for cd in range(3):
                        flattened_3x3.append(board[row_start + rd][col_start + cd])
                if not is_valid(flattened_3x3):
                    return False
        return True