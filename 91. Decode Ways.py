class Solution:
    def numDecodings(self, s: str) -> int:
        candidates = set([str(i) for i in range(1, 27)])
        # dp[i] denotes # of ways until s[i-1]
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if s[0] in candidates:
            dp[1] = 1
        
        for i in range(2, len(s)+1):
            # dp[n] = dp[n-2] * k2 + dp[n-1] * k1
            k2 = 0
            if s[i-2:i] in candidates:
                k2 += 1
            k1 = 0
            if s[i-1] in candidates:
                k1 += 1
            dp[i] = dp[i-2] * k2 + dp[i-1] * k1
        return dp[len(s)]
