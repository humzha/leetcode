class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring
        without repeating characters.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring with no duplicates.
        """
        # dp[i] = LIS of s[:i], where the LIS ends at that character
        # dp = [0 if i == 0 else None for i in range(s + 1)]

        # Starting index of the longest substring terminating at s[i - 1]
        # for computing dp(i)
        left = res = prev = 0
        chars_seen = set()

        for i in range(len(s)):
            while s[i] in chars_seen:
                chars_seen.remove(s[left])
                left += 1
            chars_seen.add(s[i])

            prev = i - left + 1
            res = max(res, prev)
        # The length of the longest substring is one of the max LIS that ends at that character s[:i]
        return res
