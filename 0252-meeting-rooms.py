class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        """
        Given an array of meeting time intervals where each interval
        is a pair [start, end], determine if a person could attend
        all meetings without any overlap. Return True if possible,
        otherwise False.

        Args:
            intervals (List[List[int]]): A list of meeting intervals
                with start and end times.

        Returns:
            bool: True if no intervals overlap, False if there is any
                conflict between meetings.
        """
        curr_end = float("-inf")
        for start, end in sorted(intervals, key=lambda x: x[0]):
            if start < curr_end:
                return False
            curr_end = max(end, curr_end)
        return True
