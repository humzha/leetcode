import collections

class Solution:
    """Solution for grouping strings that are anagrams of each other.

    Given an array of strings `strs`, group the anagrams together. Two strings
    are anagrams if they contain the same characters with the same frequency,
    but possibly in a different order. The result can be returned in any order.
    """  # :contentReference[oaicite:0]{index=0}

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Groups strings that are anagrams into sublists.

        Args:
            strs (list[str]): A list of lowercase strings.

        Returns:
            list[list[str]]: A list of groups where each group contains
                strings that are anagrams of each other.
        # All lowercase
        """
        mp = collections.defaultdict(list)
        # Hash with a count-array of 26 length, each array
        for word in strs:
            # Convert each word into an anagram-key
            count_array = [0] * 26
            for c in word:
                count_array[ord(c) - ord('a')] += 1
            mp[tuple(count_array)].append(word)
        return list(mp.values())