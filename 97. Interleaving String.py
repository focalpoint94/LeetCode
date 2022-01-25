class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.dp = set()
        return self.dfs(0, 0, 0)
        
    def dfs(self, i, j, k):
        if (i, j, k) in self.dp:
            return False
        if k == len(self.s3):
            return True
        if i < len(self.s1) and self.s1[i] == self.s3[k]:
            if self.dfs(i+1, j, k+1):
                return True
        if j < len(self.s2) and self.s2[j] == self.s3[k]:
            if self.dfs(i, j+1, k+1):
                return True
        self.dp.add((i, j, k))
        return False
