from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.wordSet = wordDict
        return self.backtrack(0)
        
    @lru_cache()    
    def backtrack(self, i):
        if i == len(self.s):
            return True
        for j in range(i+1, len(self.s)+1):
            if self.s[i:j] in self.wordSet:
                if self.backtrack(j):
                    return True
        return False
