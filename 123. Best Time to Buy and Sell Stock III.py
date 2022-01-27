class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        leftprofit, rightprofit = [0] * n, [0] * n
        
        leftmin = prices[0]
        for i in range(1, n):
            price = prices[i]
            leftmin = min(leftmin, price)
            leftprofit[i] = max(leftprofit[i-1], price - leftmin)
        
        rightmax = prices[-1]
        for i in range(n-2, -1, -1):
            price = prices[i]
            rightmax = max(rightmax, price)
            rightprofit[i] = max(rightprofit[i+1], rightmax - price)
        
        maxprofit = 0
        for i in range(n):
            maxprofit = max(maxprofit, leftprofit[i]+rightprofit[i])
        return maxprofit
