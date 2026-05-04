from collections import Counter

class Solution:
    """Solution for finding the minimum window substring.

    Given two strings s and t, return the minimum window substring of s
    such that every character in t (including duplicates) is included.
    If no such substring exists, return the empty string.
    """

    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        # running counter of the s_window
        # only monitor characters in t
        c_to_freq = Counter()
        
        def contains(c_to_freq, t_counter):
            if len(c_to_freq) < len(t_counter):
                return False
            return all([t_counter[c] <= c_to_freq[c] for c in t_counter])

        start = 0
        res, min_len = '', float('inf')
        for i, c in enumerate(s):
            if c in t_counter:
                c_to_freq[c] += 1
                while contains(c_to_freq, t_counter):
                    c_to_freq[s[start]] -= 1
                    if c_to_freq[s[start]] == 0:
                        del c_to_freq[s[start]]
                    start += 1
                    if i - start + 1 < min_len:
                        min_len = i - start + 1
                        res = s[start: i + 1]
        return res