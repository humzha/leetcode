from collections import Counter

class Solution:
    """Solution for finding the longest consecutive sequence in an unsorted array.

    Given an unsorted array of integers `nums`, return the length of the longest
    consecutive elements sequence. The algorithm must run in O(n) time.
    """

    def longestConsecutive(self, nums: list[int]) -> int:
        """Computes the longest consecutive sequence length.

        Args:
            nums (list[int]): List of integers (unsorted, may contain duplicates).

        Returns:
            int: Length of the longest consecutive sequence.
            
        Union Find Problem,

        all numbers are elements in a set, join numbers that are next to each other
        
        an edge can be drawn from every number i to i + 1 and i - 1
        """
        if not nums:
            return 0
        parent = {n: n for n in nums}
        rank = {n: 1 for n in nums}

        def find(x: int) -> int:
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> bool:
            parent_a, parent_b = find(a), find(b)
            if parent_a == parent_b:
                return False
            if rank[parent_a] > rank[parent_b]:
                parent[parent_b] = parent_a
            elif rank[parent_a] < rank[parent_b]:
                parent[parent_a] = parent_b
            else:
                rank[parent_a] += 1
                parent[parent_b] = parent_a
            return True
        
        for n in nums:
            if n + 1 in parent:
                union(n, n + 1)
            if n - 1 in parent:
                union(n, n - 1)
            
        return max(Counter([find(x) for x in list(set(nums))]).values())