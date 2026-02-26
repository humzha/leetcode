class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """
        Given an m x n image, perform a flood fill starting from
        image[sr][sc]. Change the starting pixel to the given
        color, then update all horizontally or vertically adjacent
        pixels that share the original color. Return the modified
        image.
        """

        # If the from color is the same as the to color return early
        # Without this check, will just recurse endlessly converting from_color nodes to_color when no work is nec
        if not image or not image[0] or image[sr][sc] == color:
            return image

        rows = len(image)
        cols = len(image[0])

        if sr < 0 or sc < 0 or sr >= rows or sc >= cols:
            return False

        # We don't need a visited array, it would suffice to dfs a neighbor again
        # 3 cases:
        # A node is different from the from_color
        # A node was the from color, was visited once in dfs, and is already changed
        # A node is the from_color, needs changing
        def dfs(r: int, c: int, from_color: int, to_color: int):
            if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != from_color:
                return
            image[r][c] = to_color
            for row_diff, col_diff in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(r + row_diff, c + col_diff, from_color, to_color)

        dfs(sr, sc, image[sr][sc], color)
        return image
