class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        profit = [[0] * n for _ in range(k+1)]
        for t in range(1, k+1):
            maxJ = profit[t-1][0] - prices[0]
            for i in range(n):
                maxJ = max(maxJ, profit[t-1][i] - prices[i])
                profit[t][i] = max(profit[t][i-1], prices[i] + maxJ)
        return profit[-1][-1]
