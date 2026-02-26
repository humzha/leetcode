from typing import List


class Solution:
    """Solution for determining if a string can be segmented into dictionary words.

    Given a non-empty string `s` and a dictionary `wordDict` containing a list
    of non-empty words, return `True` if `s` can be segmented into a space-
    separated sequence of one or more dictionary words. The same word in the
    dictionary may be reused multiple times in the segmentation. :contentReference[oaicite:0]{index=0}
    """

    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        """Checks if the given string can be segmented into one or more words
        from the dictionary.

        Args:
            s (str): The string to segment.
            word_dict (List[str]): The list of dictionary words.

        Returns:
            bool: True if the string can be segmented; otherwise False.
        """
        words = set(word_dict)
        dp = [None for _ in range(len(s))]

        def is_breakable(i: int) -> bool:
            """
            Checks if s[i:] is breakable into words from word_dict
            """
            if dp[i] is not None:
                return dp[i]
            dp[i] = False
            if s[i:] in words:
                dp[i] = True
            for j in range(i + 1, len(s)):
                if is_breakable(j) and s[i:j] in words:
                    dp[i] = True
            return dp[i]

        return is_breakable(0)
