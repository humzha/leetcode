class Solution:
    """Solution for generating all combinations of well-formed parentheses.

    Given `n` pairs of parentheses, return all valid combinations of balanced
    parentheses strings.
    """

    def generateParenthesis(self, n: int) -> list[str]:
        """Generates all valid parentheses combinations.

        Args:
            n (int): Number of pairs of parentheses.

        Returns:
            list[str]: All valid combinations of well-formed parentheses.
        """
        res = []
        def backtrack(l: int, r: int, path: list[str]) -> None:
            if l == r == n:
                res.append(''.join(path))
            if l < n:
                path.append('(')
                backtrack(l + 1, r, path)
                path.pop()
            if l > r:
                path.append(')')
                backtrack(l, r + 1, path)
                path.pop()

        backtrack(0, 0, [])
        return res