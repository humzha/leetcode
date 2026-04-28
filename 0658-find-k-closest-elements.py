import heapq

class Solution:
    """Solution for finding k closest elements to a target value in a sorted array.

    Given a sorted integer array `arr`, two integers `k` and `x`, return the `k`
    closest integers to `x` in the array. The result must be sorted in ascending
    order.

    An integer `a` is closer to `x` than `b` if:
    - |a - x| < |b - x|
    - If equal distance, the smaller value is preferred.
    """

    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        """Finds the k closest elements to x.

        Args:
            arr (list[int]): Sorted list of integers.
            k (int): Number of closest elements to return.
            x (int): Target value.

        Returns:
            list[int]: k closest elements sorted in ascending order.
        """
        # Keep only the k closest elements, kick out when reaches k + 1
        # we want a max_heap to get the biggest difference k + 1
        max_heap = []
        for i in range(min(k, len(arr))):
            delta = -abs(arr[i] - x)
            heapq.heappush(max_heap, (delta, -arr[i]))
            
        for i in range(k, len(arr)):
            delta = -abs(arr[i] - x)
            heapq.heappush(max_heap, (delta, -arr[i]))
            while len(max_heap) > k:
                heapq.heappop(max_heap)

        res = []
        while max_heap:
            res.append(heapq.heappop(max_heap))
        return list(sorted([x[1] * -1 for x in list(reversed(res))]))