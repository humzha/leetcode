import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return True if t is an anagram
        of s, and False otherwise.
        """
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)
        if s_counter.keys() != t_counter.keys():
            return False
        for c in s_counter.keys():
            if s_counter[c] != t_counter[c]:
                return False
        return True
