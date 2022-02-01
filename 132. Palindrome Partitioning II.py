class Solution:
    def minCut(self, s: str) -> int:
        dp = self.build_palindrome(s)
        n = len(s)
        self.cut = [2002] * n
        for end in range(n):
            if dp[0][end]:
                self.cut[end] = 0
                continue
            for start in range(1, end+1):
                if dp[start][end]:
                    self.cut[end] = min(self.cut[end], self.cut[start-1] + 1)
        return self.cut[-1]
        
    def build_palindrome(self, word):
        n = len(word)
        dp = [[False] * n for _ in range(n)]
        for end in range(n):
            for start in range(end+1):
                if word[end] == word[start] and (end - start <= 2 or dp[start+1][end-1]):
                    dp[start][end] = True
        return dp
