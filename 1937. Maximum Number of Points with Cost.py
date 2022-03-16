class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [[0] * n for _ in range(m)]
        dp[0] = points[0]
        
        for row in range(1, m):
            # forward pass
            left = 0
            for col in range(n):
                left = max(left, dp[row-1][col]+col)
                dp[row][col] = max(dp[row][col], -col+left+points[row][col])
            
            # backward pass
            right = dp[row-1][n-1]-(n-1)
            for col in range(n-1, -1, -1):
                right = max(right, dp[row-1][col]-col)
                dp[row][col] = max(dp[row][col], col+right+points[row][col])
            
        return max(dp[-1])
