class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(i: int, j: int, word_idx: int) -> bool:
            if word_idx == len(word):
                return True
            if i < 0 or j < 0 or i >= rows or j >= cols or visited[i][j]:
                return False

            if board[i][j] == word[word_idx]:
                visited[i][j] = True
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nr, nc = i + dr, j + dc
                    if dfs(nr, nc, word_idx + 1):
                        visited[i][j] = False
                        return True
                visited[i][j] = False
            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
