import string
from functools import lru_cache
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        
        N = len(words[0])
        freqs = [{c: 0 for c in string.ascii_lowercase} for _ in range(N)]
        
        for word in words:
            for i, c in enumerate(word):
                freqs[i][c] += 1

        @lru_cache(None)
        def dfs(i, j):
            nonlocal N, target
            if i == len(target):
                return 1
            if j == N:
                return 0

            return (freqs[j][target[i]] * dfs(i+1, j+1) + dfs(i, j+1)) % (10**9+7)

        return dfs(0, 0)
