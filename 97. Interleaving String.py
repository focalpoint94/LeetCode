from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        self.s1, self.s2, self.s3 = s1, s2, s3
        return self.backTrack(0, 0)
        
    @lru_cache()
    def backTrack(self, p1, p2):
        if p1 + p2 == len(self.s3):
            return True
        
        if p1 < len(self.s1) and self.s3[p1+p2] == self.s1[p1]:
            if self.backTrack(p1+1, p2):
                return True
        
        if p2 < len(self.s2) and self.s3[p1+p2] == self.s2[p2]:
            if self.backTrack(p1, p2+1):
                return True
            
        return False
