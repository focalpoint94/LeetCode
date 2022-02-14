class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        from collections import defaultdict
        ret = 0
        for i, t in enumerate(time):
            time[i] = t % 60
        dic = defaultdict(int)
        for t in time:
            ret += dic[0] if t == 0 else dic[60-t]
            dic[t] += 1
        return ret
