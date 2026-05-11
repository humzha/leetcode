class Solution:
    """Solution for finding the minimum ship capacity to ship packages within D days.

    Given an array of package weights and an integer days, return the
    least weight capacity of the ship that will allow all packages to be
    shipped in the given order within the specified number of days.
    """

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        # Your implementation here
        def ship(weight_capacity: int) -> bool:
            """
            Can ship all packages with this weight limit by the specified
            number of days
            
            We must load the ship wioth packages on the conveyer belt in the order
            given in weights
            """
            days_spent = 1
            day_weight = 0
            for w in weights:
                day_weight += w
                if day_weight > weight_capacity:
                    days_spent += 1
                    day_weight = w
            return days_spent <= days
        l, r  = max(weights), sum(weights)

        while l < r:
            m = (l + r) // 2
            if ship(m):
                r = m
            else:
                l = m + 1
        return l