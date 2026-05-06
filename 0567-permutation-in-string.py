from collections import Counter

class Solution:
    """Solution for checking if a string contains a permutation of another.

    Given two strings s1 and s2, return true if s2 contains a permutation
    of s1 as a substring, or false otherwise.
    """
    

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])
        
        if s1_counter == s2_counter:
            return True
        # 012
        # 0123
        # j = 3
        for j in range(len(s1), len(s2)):
            # Update sliding window
            new_c = s2[j]
            old_c = s2[j - len(s1)]
            s2_counter[new_c] += 1
            s2_counter[old_c] -= 1
            if s2_counter[old_c] == 0:
                del s2_counter[old_c]
            if s1_counter == s2_counter:
                return True
        return False