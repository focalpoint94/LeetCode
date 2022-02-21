class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for timePoint in timePoints:
            hour, minute = list(map(int, timePoint.split(':')))
            time = hour * 60 + minute
            times.append(time)
            times.append(time + 24 * 60)
        times.sort()
        ret = 24 * 60
        prev = times[0]
        for i in range(1, len(times)):
            ret = min(ret, times[i] - prev)
            prev = times[i]
        return ret
