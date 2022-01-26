class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, low = 0, float('inf')
        for price in prices:
            low = min(low, price)
            profit = max(profit, price-low)
        return profit
