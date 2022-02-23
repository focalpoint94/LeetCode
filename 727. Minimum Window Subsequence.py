class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s2), len(s1)
        dp = [[-1] * n for _ in range(m)]
        if s1[0] == s2[0]:
            dp[0][0] = 0
        for i in range(1, n):
            if s2[0] == s1[i]:
                dp[0][i] = i
            else:
                dp[0][i] = dp[0][i-1]
        for i in range(1, m):
            for j in range(1, n):
                if s1[j] == s2[i]:
                    dp[i][j] = max(dp[i-1][j-1], dp[i][j-1])
                else:
                    dp[i][j] = dp[i][j-1]
        if dp[-1][-1] == -1:
            return ""
        minlength, ret = len(s1) + 1, ''
        for i in range(n):
            if dp[-1][i] != -1 and i - dp[-1][i] + 1 < minlength:
                minlength = i - dp[-1][i] + 1
                ret = s1[dp[-1][i]:i+1]
        return ret
