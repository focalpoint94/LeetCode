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

# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         newIntervals = []
#         i = 0
#         for i in range(len(intervals)):
#             interval = intervals[i]
#             if interval[0] <= newInterval[0]:
#                 newIntervals.append(interval)
#             else:
#                 break
        
#         if newIntervals and newInterval[0] <= newIntervals[-1][1]:
#             newIntervals[-1][1] = max(newIntervals[-1][1], newInterval[1])
#         else:
#             newIntervals.append(newInterval)
        
#         for j in range(i, len(intervals)):
#             interval = intervals[j]
#             if interval[0] <= newIntervals[-1][1]:
#                 newIntervals[-1][1] = max(newIntervals[-1][1], interval[1])
#             else:
#                 newIntervals.append(interval)
        
#         return newIntervals
