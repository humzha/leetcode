class Solution:
    """Solution for determining the maximum amount of money that can be robbed
    without alerting the police.

    You are a professional robber planning to rob houses along a street. Each
    house has a non‑negative amount of money. Adjacent houses have security
    systems connected, so **robbed houses must not be adjacent**. Return the
    maximum amount of money you can rob without triggering the alarms.
    """

    def rob(self, nums: list[int]) -> int:
        """Calculates the maximum robbery total given non‑adjacent constraints.

        Args:
            nums (List[int]): A list of non‑negative integers representing
                money at each house.

        Returns:
            int: The maximum amount that can be robbed.
        """
        p = pp = 0
        for n in nums:
            curr = max(pp + n, p)
            p, pp = curr, p
        return max(p, pp)