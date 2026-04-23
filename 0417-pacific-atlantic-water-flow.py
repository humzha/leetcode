class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
            
        def dfs(from_height: int, r: int, c: int, visited: set[tuple[int, int]]) -> None:
            """
            Populates the visited set with all the elements that can be filled from heights[r][c]
            """
            # height[r][c] (to): 87
            # from: 86
            # 87 >= 86, can flow 
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or heights[r][c] < from_height:
                return

            visited.add((r, c))
            dfs(heights[r][c], r + 1, c, visited)
            dfs(heights[r][c], r - 1, c, visited)
            dfs(heights[r][c], r, c + 1, visited)
            dfs(heights[r][c], r, c - 1, visited)
            
        def visit(coords: list[tuple[int, int]]) -> set[tuple[int, int]]:
            visited = set()
            for r, c in coords:
                dfs(heights[r][c], r, c, visited)
            return visited

        atlantic = []
        pacific = []
        for j in range(cols):
            atlantic.append((rows - 1, j))
            pacific.append((0, j))
        for i in range(rows):
            atlantic.append((i, cols - 1))
            pacific.append((i, 0))

        visited_both = visit(atlantic) & visit(pacific)
        return [list(coord) for coord in visited_both]