import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ret = 0
        intervals.sort()
        q = []
        for s, e in intervals:
            while q and q[0] <= s:
                heapq.heappop(q)
            heapq.heappush(q, e)
            ret = max(ret, len(q))
        return ret
