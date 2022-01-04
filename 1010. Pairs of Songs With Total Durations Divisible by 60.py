class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [t % 60 for t in time]
        from collections import Counter
        c = Counter()
        ans = 0
        for t in time:
            ans += c[60-t] if t > 0 else c[0]
            c[t] += 1
        return ans
