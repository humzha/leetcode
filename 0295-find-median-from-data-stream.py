import heapq

class MedianFinder:
    """Data structure that supports adding numbers and finding the median.

    Supports adding numbers from a data stream and returning the median
    of all elements seen so far in O(log n) time per addition.
    """

    def __init__(self):
        # Your implementation here
        self.min_heap = []
        self.max_heap = []
        pass

    def addNum(self, num: int) -> None:
        # Push into min_heap
        heapq.heappush(self.min_heap, num)
        # Push min from min_heap into max_heap
        heapq.heappush(self.max_heap, heapq.heappop(self.min_heap) * -1)
        # Push max from max_heap into min_heap
        heapq.heappush(self.min_heap, heapq.heappop(self.max_heap) * -1)
        
        if len(self.min_heap) - len(self.max_heap) == 2:
            heapq.heappush(self.max_heap, heapq.heappop(self.min_heap) * -1)

        pass

    def findMedian(self) -> float:
        # Your implementation here
        if not self.min_heap and not self.max_heap:
            return -1.0
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 1:
            return self.min_heap[0]
        return (self.min_heap[0] + (self.max_heap[0] * -1)) / 2