import math
from typing import List, Tuple
import heapq


def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        Given an array of points where points[i] = [x_i, y_i] represents
        a point on the 2D plane, return the k closest points to the origin
        (0, 0). The distance is computed using the Euclidean distance.

        Args:
            points (List[List[int]]): List of points [x, y].
            k (int): Number of closest points to return.

        Returns:
            List[List[int]]: The k closest points to the origin.
        """
        # (euclid_distance, (x, y))
        min_heap: List[Tuple[float, int, int]] = []
        for x, y in points:
            heapq.heappush(min_heap, (euclidean_distance(x, y, 0, 0), x, y))
        return [(x[1], x[2]) for x in heapq.nsmallest(k, min_heap)]
