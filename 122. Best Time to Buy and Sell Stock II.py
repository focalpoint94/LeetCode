class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        prev = prices[0]
        for i in range(1, len(prices)):
            ret += max(prices[i]-prev, 0)
            prev = prices[i]
        return ret
