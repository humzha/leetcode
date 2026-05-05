class Solution:
    """Solution for maximizing profit with multiple stock transactions.

    Given an integer array prices where prices[i] is the price on the ith day,
    return the maximum profit you can achieve by buying and selling the stock
    multiple times. You can only hold at most one share at any time.
    """

    def maxProfit(self, prices: list[int]) -> int:
        # given that there is no limitation on # sales
        # compare every day to the next
        # if today is less than tomorrow, buy today, sell tomorrow
        # repeat for all pairs of numbers [i, i + 1]
        res = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                res += prices[i + 1] - prices[i]
        return res