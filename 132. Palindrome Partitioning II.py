class Solution:
    def minCut(self, s: str) -> int:
        palin = self.palindrome(s)
        dp = [2002] * len(s)
        dp[0] = 0
        for i in range(1, len(s)):
            if palin[0][i]:
                dp[i] = 0
                continue
            for j in range(1, i+1):
                if palin[j][i]:
                    dp[i] = min(dp[i], dp[j-1]+1)
        return dp[-1]
    
    def palindrome(self, word):
        n = len(word)
        table = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(j+1):
                if word[j] == word[i] and (j - i <= 2 or table[i+1][j-1]):
                    table[i][j] = True
        return table
        
