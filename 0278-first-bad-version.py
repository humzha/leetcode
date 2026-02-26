# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Given n versions [1, 2, ..., n] and an API isBadVersion(version)
        that returns whether a version is bad, find the first bad version.

        Args:
            n (int): The total number of versions.

        Returns:
            int: The version number of the first bad version.
        """
        l, r = 1, n
        # 12345
        # B
        #   m
        # r = m
        # l = m + 1
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l
