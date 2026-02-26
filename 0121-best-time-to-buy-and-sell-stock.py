class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
        # minimum price seen yesterday or days before
        prev_price = prices[0]
        max_profit = 0
        for n in prices[1:]:
            prev_price = min(prev_price, n)
            max_profit = max(n - prev_price, max_profit)
        return max_profit
