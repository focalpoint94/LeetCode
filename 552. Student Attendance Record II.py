class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [0, 1, 1, 0, 0, 1]
        if n == 1:
            return sum(dp)
        
        for i in range(2, n+1):
            next_dp = [0] * len(dp)
            next_dp[0] = dp[1] % (10**9+7)
            next_dp[1] = dp[2] % (10**9+7)
            next_dp[2] = (dp[0] + dp[1] + dp[2]) % (10**9+7)
            next_dp[3] = dp[4] % (10**9+7)
            next_dp[4] = dp[5] % (10**9+7)
            next_dp[5] = (dp[0] + dp[1] + dp[2] + dp[3] + dp[4] + dp[5]) % (10**9+7)
            dp = next_dp
        return sum(dp) % (10**9+7)
        
