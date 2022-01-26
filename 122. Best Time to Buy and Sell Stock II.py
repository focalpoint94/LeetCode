class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, prev = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] >= prev:
                profit += prices[i] - prev
            prev = prices[i]
        return profit
