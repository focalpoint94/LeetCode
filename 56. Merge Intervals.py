class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        ret = []
        for interval in intervals:
            if ret and ret[-1][0] <= interval[0] <= ret[-1][1]:
                ret[-1][1] = max(ret[-1][1], interval[1])
            else:
                ret.append(interval)
        return ret
