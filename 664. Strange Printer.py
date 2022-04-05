class Solution:
    def strangePrinter(self, s: str) -> int:
        N = len(s)
        dp = [[N] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = 1
        for length in range(2, len(s)+1):
            for i in range(len(s)-length+1):
                end = i + length - 1
                for j in range(i+1, end+1):
                    if s[i] == s[end]:
                        dp[i][end] = min(dp[i][end], dp[i][j-1] + dp[j][end] - 1)
                    else:
                        dp[i][end] = min(dp[i][end], dp[i][j-1] + dp[j][end])
        return dp[0][-1]
