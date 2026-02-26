from typing import List


class Solution:
    """Solution for finding the container that holds the most water.

    You are given an integer array `height` where `height[i]` represents the
    height of a vertical line at position `i`. The width between each pair of
    lines is 1. Find two lines that together with the x-axis form a container,
    such that the container holds the most water (maximizes area). Return the
    maximum area of water the container can store.
    """

    def maxArea(self, height: List[int]) -> int:
        """Calculates the maximum area between two lines in the height array.

        Args:
            height (List[int]): A list of non-negative integers representing line heights.

        Returns:
            int: The maximum water area that can be contained.
        """
        res = area = 0
        l, r = 0, len(height) - 1
        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res
