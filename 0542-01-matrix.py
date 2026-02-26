import collections


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Given a matrix mat consisting of 0s and 1s, return a matrix
        where each cell contains the distance to the nearest 0.
        The distance between adjacent cells is 1.

        Args:
            mat (List[List[int]]): A 2D binary matrix.

        Returns:
            List[List[int]]: A matrix of the same size where each
            element is the distance to the nearest 0.
        """
        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])

        # Multi-source BFS from all [(0, 0)]
        res = [[None for _ in range(cols)] for _ in range(rows)]
        q = collections.deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    # (row_idx, col_idx, distance)
                    q.append((i, j, 0))
                    res[i][j] = 0

        # visited[i][j] = res[i][j] is not None
        while q:
            row_idx, col_idx, distance = q.popleft()

            for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                nei_row, nei_col = row_idx + dr, col_idx + dc
                if (
                    0 <= nei_row < rows
                    and 0 <= nei_col < cols
                    and res[nei_row][nei_col] is None
                ):
                    q.append((nei_row, nei_col, distance + 1))
                    res[nei_row][nei_col] = distance + 1
        return res
