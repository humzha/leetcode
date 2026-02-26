class Solution:
    def insert(
        self,
        intervals: list[list[int]],
        new_interval: list[int],
    ) -> list[list[int]]:
        """
        Given a list of non-overlapping intervals sorted by start time,
        insert a new interval into the list and merge if necessary. Return
        the resulting list of intervals sorted by start time.

        Args:
            intervals (List[List[int]]): A list of sorted, non-overlapping intervals.
            new_interval (List[int]): The interval to insert.

        Returns:
            List[List[int]]: The list of merged intervals after insertion.
        """

        # We can divide the subarray into 3 parts
        # - BEFORE (can be empty)
        # - INTERVALS_OVERlAP_WITH_NEW
        # - AFTER (can be empty)

        # BEFORE
        # curr = (1, 2)
        # insert = (6, 7) 2 < 6
        # curr.end < insert.start

        # MERGE
        # curr = (-1, 3)
        # insert = (2, 5) 3 >= 2
        # curr.end >= insert.start

        # AFTER
        # curr = (-1, 3)
        # insert = (6, 7) 3 < 7
        # curr.end < insert.start

        # BEFORE
        res = []
        before_idx = -1
        for i, curr in enumerate(intervals):
            if curr[1] < new_interval[0]:
                res.append(curr)
                before_idx = i
            else:
                break

        # MERGE subarray may not have any members
        merge_idx = before_idx
        for i, curr in enumerate(intervals[before_idx + 1 :], start=before_idx + 1):
            if new_interval[1] >= curr[0]:
                new_interval = [
                    min(new_interval[0], curr[0]),
                    max(new_interval[1], curr[1]),
                ]
                merge_idx = i

        # Account for merge subarray being empty
        res.append(new_interval)
        res.extend(intervals[merge_idx + 1 :])
        return res
