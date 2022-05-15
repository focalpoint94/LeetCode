class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        end = 0
        for interval in intervals:
            if interval[0] < end:
                return False
            end = interval[1]
        return True
