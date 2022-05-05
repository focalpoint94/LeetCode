class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.isPalin = self.palindrome(s)
        self.s = s
        self.ret = []
        self.dfs(0, [])
        return self.ret
        
    def dfs(self, i, path):
        if i == len(self.s):
            self.ret.append(path)
            return
        for j in range(i, len(self.s)):
            if self.isPalin[i][j]:
                self.dfs(j+1, path+[self.s[i:j+1]])
        
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
