class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        leftProfit, rightProfit = [0] * n, [0] * n
        
        leftMin = prices[0]
        for i in range(1, n):
            leftMin = min(leftMin, prices[i])
            leftProfit[i] = max(leftProfit[i-1], prices[i]-leftMin)
        
        rightMax = prices[-1]
        for i in range(n-2, -1, -1):
            rightMax = max(rightMax, prices[i])
            rightProfit[i] = max(rightProfit[i+1], rightMax-prices[i])
        
        return max(p1 + p2 for p1, p2 in zip(leftProfit, rightProfit))
