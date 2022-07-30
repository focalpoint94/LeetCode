class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ret, covered = 0, -1
        for t in timeSeries:
            if covered < t:
                ret += duration
            else:
                ret += max(0, t + duration - 1 - covered)
            covered = max(covered, t + duration - 1)
        return ret
