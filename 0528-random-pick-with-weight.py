from random import random

class Solution:
    """Solution for randomly picking an index with probability proportional to weight.

    You are given an array `w` where `w[i]` represents the weight of index `i`.
    Implement `pickIndex()` such that the probability of returning index `i`
    is proportional to `w[i] / sum(w)`.
    """

    def __init__(self, w: list[int]):
        """Initializes the object with weights.

        Args:
            w (list[int]): List of positive weights.
        """
        self.cumulative_weights = []
        acc = 0
        for i in range(len(w)):
            acc += w[i]
            self.cumulative_weights.append(acc)

    def pickIndex(self) -> int:
        """Returns a random index based on weight distribution.

        Returns:
            int: Random index where probability is proportional to weight.
        """
        target = random() * self.cumulative_weights[-1]
        # bisect_left
        l = 0
        r = len(self.cumulative_weights) - 1
        while l < r:
            m = (l + r) // 2
            if target > self.cumulative_weights[m]:
                l = m + 1
            else:
                r = m
        return l
