class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ret = 0
        for i in range(1, len(timeSeries)):
            ret += min(timeSeries[i]-timeSeries[i-1], duration)
        ret += duration
        return ret
