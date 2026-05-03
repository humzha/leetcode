class Solution:
    """Solution for counting combinations that sum to a target.

    Given an array of distinct integers nums and a target integer target,
    return the number of possible combinations that add up to target.
    Different sequences are counted as different combinations.
    """

    def combinationSum4(self, nums: list[int], target: int) -> int:
        # Your implementation here
        dp = [1 if i == target else None for i in range(target + 1)]
        def f(x: int) -> int:
            if x > target:
                return 0
            if dp[x] is None:
                res = 0
                for n in nums:
                    res += f(x + n)
                dp[x] = res
            return dp[x]
        return f(0)
