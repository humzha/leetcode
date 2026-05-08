import math

class Solution:
    """Solution for finding the minimum eating speed to finish all bananas.

    Given n piles of bananas and h hours before the guards return,
    return the minimum integer eating speed k such that Koko can eat
    all bananas within h hours.
    """

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def can_eat(k: int) -> bool:
            hours_taken = 0
            for food in piles:
                hours_taken += math.ceil(food / k)
                if hours_taken > h:
                    return False
            return True
        l = 1
        r = max(piles)
        while l < r:
            m = (l + r) // 2
            if can_eat(m):
                r = m
            else:
                l = m + 1
        return l