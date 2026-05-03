class Solution:
    """Solution for finding the minimum number of intervals to remove.

    Given an array of intervals, return the minimum number of intervals
    to remove to make the rest non-overlapping. Intervals that touch
    only at a point are considered non-overlapping.
    """

    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # Your implementation here
        intervals.sort(key=lambda x: x[0])
        removed_intervals = 0
        prev_end = float('-inf')
        for start, end in intervals:
            # Remove prev interval
            if prev_end > start:
                removed_intervals += 1
                # Keep the interval with the smalleer end
                prev_end = min(prev_end, end)
            else:
                prev_end = end
        return removed_intervals