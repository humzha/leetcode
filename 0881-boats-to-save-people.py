class Solution:
    """Solution for finding the minimum number of boats to save people.

    Given an array people where people[i] is the weight of the ith person
    and an integer limit representing the maximum weight each boat can carry,
    return the minimum number of boats needed to carry everyone.
    Each boat carries at most two people with combined weight <= limit.
    """

    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # Your implementation here
        # Assume every person weighs less than the max limit of a boat
        people.sort()
        boat_weight = occupants =  0
        boats = 1
        l, r = 0, len(people) - 1
        while l <= r:
            if occupants == 2:
                boats += 1
                boat_weight = occupants = 0
                continue 

            if boat_weight + people[r] <= limit:
                boat_weight += people[r]
                occupants += 1
                r -= 1
            elif boat_weight + people[l] <= limit:
                boat_weight += people[l]
                occupants += 1
                l += 1
            else:
                boats += 1
                boat_weight = occupants = 0
        return boats
            