class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        decoder = {str(i): chr(i+64) for i in range(1, 27)}
        N = len(s)
        dp = [0] * (N+1)
        dp[0] = dp[1] = 1
        
        for i in range(2, N+1):
            if s[i-1] in decoder:
                dp[i] += dp[i-1]
            if s[i-2:i] in decoder:
                dp[i] += dp[i-2]
        return dp[-1]
