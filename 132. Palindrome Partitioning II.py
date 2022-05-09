class Solution:
    def minCut(self, s: str) -> int:
        N = len(s)
        palin = self.palindrome(s)
        dp = [N] * N
        dp[0] = 0
        for i in range(1, N):
            if palin[0][i]:
                dp[i] = 0
            else:
                dp[i] = dp[i-1] + 1
                for j in range(i):
                    if palin[j+1][i]:
                        dp[i] = min(dp[i], dp[j]+1)
        return dp[-1]
        
    def palindrome(self, s):
        N = len(s)
        isPalin = [[False] * N for _ in range(N)]
        for i in range(N):
            isPalin[i][i] = True
        for i in range(N-1):
            if s[i] == s[i+1]:
                isPalin[i][i+1] = True
        for length in range(3, N+1):
            for i in range(N):
                j = i + length - 1
                if j <= len(s) - 1 and isPalin[i+1][j-1] and s[i] == s[j]:
                    isPalin[i][j] = True
        return isPalin
