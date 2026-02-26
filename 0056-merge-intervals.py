from typing import List


class Solution:
    """Solution for merging all overlapping intervals in a list.

    Given an array of intervals where intervals[i] = [start_i, end_i], merge all
    overlapping intervals and return an array of the non-overlapping intervals
    that cover all the intervals in the input.:contentReference[oaicite:0]{index=0}
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Returns a list of merged intervals.

        Args:
            intervals (List[List[int]]): A list of intervals where each interval
                is a list of two integers representing [start, end].

        Returns:
            List[List[int]]: A list of intervals after merging all overlapping
                intervals.
        """
        res = []
        intervals.sort(key=lambda x: x[0])
        for start, end in intervals:
            if res and res[-1][1] >= start:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res
