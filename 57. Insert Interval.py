class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        i = 0
        for i, interval in enumerate(intervals):
            if interval[0] <= newInterval[0]:
                ret.append(interval)
            else:
                break
        
        if ret and ret[-1][1] >= newInterval[0]:
            ret[-1][1] = max(ret[-1][1], newInterval[1])
        else:
            ret.append(newInterval)
            
        for j in range(i, len(intervals)):
            interval = intervals[j]
            if ret and ret[-1][1] >= interval[0]:
                ret[-1][1] = max(ret[-1][1], interval[1])
            else:
                ret.append(interval)
        return ret
