from typing import List


class Solution:
    """Solution for generating all subsets (the power set) of a list of distinct integers.

    Given an integer array `nums` of **distinct** integers, return *all possible
    subsets* (the power set). The solution set **must not** contain duplicate
    subsets. You may return the answer in **any order**.
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Generates all subsets of the input list.

        Args:
            nums (List[int]): A list of distinct integers.

        Returns:
            List[List[int]]: A list of all possible subsets.
        """
        res = []

        def dfs(i: int, path: List[int]):
            if i == len(nums):
                res.append(path.copy())
                return
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
            dfs(i + 1, path)

        dfs(0, [])
        return res
