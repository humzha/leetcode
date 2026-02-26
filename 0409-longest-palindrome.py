import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Given a string s of lowercase and uppercase letters, return
        the *length* of the longest palindrome that can be built
        using those letters. Letters are case sensitive.
        """

        # abccccdd
        c_freqs = collections.Counter(s).values()
        res = 0
        for freq in c_freqs:
            if res % 2 == 0 and freq % 2 == 1:
                res += 1
            if freq % 2 == 1:
                res += freq - 1
            else:
                res += freq
        return res
