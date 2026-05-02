class Solution:
    """Solution for counting the number of ways to decode a numeric string.

    A message containing letters from A-Z is encoded as:
    'A' -> 1, 'B' -> 2, ..., 'Z' -> 26.

    Given a string `s` containing only digits, return the total number
    of ways to decode it.
    """

    def numDecodings(self, s: str) -> int:
        """Counts the number of valid decodings.

        Args:
            s (str): Encoded string of digits.

        Returns:
            int: Number of possible decodings.
        """
        dp = [None for _ in range(len(s))]
        # 1 <= 26 is valid
        # no leading 0's
        def dfs(i: int) -> int:
            if i >= len(s):
                return 1
            if dp[i] is None:
                dp[i] = 0
                if s[i] == '0':
                    return 0
                else:
                    dp[i] += dfs(i + 1)
                    if i <= len(s) - 2 and 10 <= int(s[i: i + 2]) <= 26:
                        dp[i] += dfs(i + 2)
            return dp[i]
        return dfs(0)