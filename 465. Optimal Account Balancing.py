from itertools import combinations
import functools

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        money = [0] * 12
        for f, t, m in transactions:
            money[f] -= m
            money[t] += m
        self.money = [m for m in money if m != 0]
        idxs = tuple([i for i in range(len(self.money))])
        return self.helper(idxs)
    
    @lru_cache()
    def helper(self, idxs):
        if not idxs:
            return 0
        ret = len(idxs) - 1
        for k in range(2, len(idxs)//2+1):
            for temp in combinations(idxs, k):
                if sum([self.money[i] for i in temp]) == 0:
                    rest = tuple(set(idxs) - set(temp))
                    ret = min(ret, self.helper(rest) + k - 1)
        return ret
