class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        from bisect import insort
        idx = insort(intervals, newInterval)
        ret = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if ret[-1][1] >= interval[0]:
                ret[-1][1] = max(ret[-1][1], interval[1])
            else:
                ret.append(interval)
        return ret
