class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        from bisect import bisect_left
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        ret = []
        for w, h in envelopes:
            idx = bisect_left(ret, h)
            if idx == len(ret):
                ret.append(h)
            else:
                ret[idx] = h
        return len(ret)
