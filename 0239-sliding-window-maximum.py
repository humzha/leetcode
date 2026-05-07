from collections import deque

class Solution:
    """Solution for finding the maximum value in each sliding window.

    Given an array of integers nums and a sliding window of size k
    moving from left to right, return the maximum value in each window.
    """

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # Your implementation here
        # Queue of all max candidates
        # Monotonically decreasing stack
        # 8 7 6
        # 8 8 6

        q = deque()
        for i in range(k):
            # nums[i] is a better candidate than all of them
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])

        res = [q[0]]
        # 0 1 2 3 k = 3
        #       i
        # 3 - 3 = 0
        for i in range(k, len(nums)):
            if nums[i - k] == q[0]:
                q.popleft()
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            res.append(q[0])

        return res