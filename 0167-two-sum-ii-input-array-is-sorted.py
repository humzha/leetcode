class Solution:
    """Solution for finding two numbers that sum to a target in a sorted array.

    Given a 1-indexed array of integers numbers sorted in non-decreasing order,
    return the indices (1-indexed) of two numbers that add up to target.
    """

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Your implementation here
        l, r = 0, len(numbers) - 1
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum > target:
                r -= 1
            elif curr_sum == target:
                return [l + 1, r + 1]
            else:
                l += 1
        return (-1, -1)