class Solution:
    """Solution for finding the longest palindromic substring.

    Given a string `s`, return the longest substring of `s` that is a palindrome.
    A substring is a contiguous sequence of characters within the string.
    """

    def longestPalindrome(self, s: str) -> str:
        """Returns the longest palindromic substring in the input string.

        Args:
            s (str): The input string.

        Returns:
            str: The longest palindrome substring.
        """
        if len(s) <= 1:
            return s

        # Base Case 1/2
        n = len(s)
        res = s[0]
        dp = [[i == j for j in range(n)] for i in range(n)]

        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            if dp[i][i + 1]:
                res = s[i : i + 2]

        for curr_len in range(3, len(s) + 1):
            for l in range(len(s) - curr_len + 1):
                r = l + curr_len - 1
                dp[l][r] = s[l] == s[r] and dp[l + 1][r - 1]

                if dp[l][r]:
                    res = s[l : r + 1]
        return res
