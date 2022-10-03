from functools import lru_cache
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordSet = set(words)
        
        @lru_cache(None, None)
        def dfs(word):
            if len(word) == 1:
                return 1
            ret = 1
            for i in range(len(word)):
                candidate = word[:i] + word[i+1:]
                if candidate in wordSet:
                    ret = max(ret, dfs(candidate) + 1)
            return ret
        
        ret = 0
        for word in words:
            ret = max(ret, dfs(word))
        return ret
