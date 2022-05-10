import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        h = []
        ret = 0
        for interval in intervals:
            while h and h[0] <= interval[0]:
                heapq.heappop(h)
            heapq.heappush(h, interval[1])
            ret = max(ret, len(h))
        return ret
