class Solution:
    def strangePrinter(self, s: str) -> int:
        S = ''.join(a for a, b in zip(s, '#' + s) if a != b)
        n = len(s)
        dp = [[n] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for length in range(2, n+1):
            for i in range(n):
                j = i + length - 1
                if j >= n:
                    break
                if s[i] == s[j]:
                    for k in range(j):
                        dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]-1)
                else:
                    for k in range(j):
                        dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j])
        return dp[0][-1]
