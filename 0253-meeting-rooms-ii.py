import heapq

class Solution:
    """Solution for finding the minimum number of meeting rooms required.

    Given an array of meeting time intervals `intervals` where each interval
    is [start, end], return the minimum number of conference rooms required
    so that all meetings can take place without overlapping.
    """

    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        """Computes the minimum number of meeting rooms.

        Args:
            intervals (list[list[int]]): List of meeting intervals.

        Returns:
            int: Minimum number of rooms required.
        """
        end_times = []
        res = 0
        intervals.sort(key=lambda x: x[0])
        for start, end in intervals:
            while end_times and end_times[0] <= start:
                heapq.heappop(end_times)
            heapq.heappush(end_times, end)
            res = max(res, len(end_times))
        return res
    
def run_tests():
    # cba clanker made this
    s = Solution()

    # Basic cases
    assert s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert s.minMeetingRooms([[7, 10], [2, 4]]) == 1

    # No overlap
    assert s.minMeetingRooms([[1, 2], [3, 4], [5, 6]]) == 1

    # Fully overlapping
    assert s.minMeetingRooms([[1, 10], [2, 9], [3, 8], [4, 7]]) == 4

    # Same start times
    assert s.minMeetingRooms([[1, 5], [1, 3], [1, 4]]) == 3

    # Touching intervals
    assert s.minMeetingRooms([[1, 5], [5, 10], [10, 15]]) == 1

    # Nested overlaps
    assert s.minMeetingRooms([[1, 10], [2, 3], [4, 5], [6, 7], [8, 9]]) == 2

    # Single meeting
    assert s.minMeetingRooms([[1, 5]]) == 1

    # Empty input
    assert s.minMeetingRooms([]) == 0

    # Overlap spike
    assert s.minMeetingRooms([[1, 4], [2, 5], [3, 6], [4, 7]]) == 3

    # Random-ish case
    assert s.minMeetingRooms([[13,15],[1,13],[6,9],[2,10],[5,7]]) == 4

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()