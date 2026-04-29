from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def get_max_c(mp: dict[str, int]) -> str:
            # mp is guaranteed to not be empty
            if len(mp) == 0:
                raise ValueError()

            max_freq = 0
            res = None
            for c, freq in mp.items():
                if freq > max_freq:
                    res = c
            return res

        c_to_freq = defaultdict(int)
        start = res = 0
        for i in range(len(s)):
            c_to_freq[s[i]] += 1
            # window_len = i - start + 1
            while i - start + 1 > max(c_to_freq.values()) + k:
                c_to_freq[s[start]] -= 1
                if c_to_freq[s[start]] == 0:
                    del c_to_freq[s[start]]
                start += 1
            res = max(res, i - start + 1)

        return res