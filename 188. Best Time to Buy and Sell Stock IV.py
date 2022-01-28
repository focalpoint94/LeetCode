class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * (n) for _ in range(k+1)]
        ret = 0
        for i in range(1, k+1):
            prevprofit = -prices[0]
            for j in range(1, n):
                prevprofit = max(prevprofit, dp[i-1][j] - prices[j])
                dp[i][j] = max(dp[i][j-1], prevprofit + prices[j])
                ret = max(ret, dp[i][j])
        return ret
