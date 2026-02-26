from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Given an array of distinct coin denominations and a total
        amount, return the fewest number of coins that add up to
        that amount. If the amount cannot be formed with the given
        coins, return -1.

        Args:
            coins (List[int]): Available coin denominations.
            amount (int): The target amount.

        Returns:
            int: The minimum number of coins to make up amount,
                or -1 if it cannot be formed.
        """
        # Given amount a,
        # We can compose a combination from each coin denomination we have
        # dp[i] = None denotes that it is uncomposable from the denominations we have
        dp = [0 if i == 0 else None for i in range(amount + 1)]
        coins.sort()
        for a in range(1, amount + 1):
            coins_needed = float("inf")
            for denomination in coins:
                if a - denomination < 0:
                    break
                elif dp[a - denomination] is None:
                    continue
                else:
                    coins_needed = min(coins_needed, 1 + dp[a - denomination])

            if coins_needed != float("inf"):
                dp[a] = coins_needed

        if dp[amount] is None:
            return -1
        return dp[amount]
