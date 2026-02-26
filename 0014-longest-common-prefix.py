class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Given an array of strings, find the longest common prefix
        shared among all strings. If there is no common prefix,
        return an empty string.

        Args:
            strs (List[str]): A list of input strings.

        Returns:
            str: The longest common prefix among the strings.
        """
        n = min([len(s) for s in strs])
        common_prefix = []
        for i in range(n):
            if not all(s[i] == strs[0][i] for s in strs):
                return "".join(common_prefix)
            else:
                common_prefix.append(strs[0][i])

        return "".join(common_prefix)
