import heapq

class Solution:
    """Solution for finding the kth largest element in an unsorted array.

    Given an integer array `nums` and an integer `k`, return the kth largest
    element in the array.

    Note:
    - It is the kth largest element in sorted order, not the kth distinct element.
    """

    def findKthLargest(self, nums: list[int], k: int) -> int:
        """Finds the kth largest element in the array.

        Args:
            nums (list[int]): List of integers.
            k (int): The kth position.

        Returns:
            int: The kth largest element.
        """
        heap = []
        for i in range(k):
            heapq.heappush(heap, nums[i])
        for i in range(k, len(nums)):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]