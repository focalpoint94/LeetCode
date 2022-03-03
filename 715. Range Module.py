class RangeModule:
    from bisect import bisect
    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        insort(self.intervals, [left, right])
        ret = [self.intervals[0]]        
        for i in range(1, len(self.intervals)):
            interval = self.intervals[i]
            if ret[-1][1] >= interval[0]:
                ret[-1][1] = max(ret[-1][1], interval[1])
            else:
                ret.append(interval)
        self.intervals = ret
        
    def queryRange(self, left: int, right: int) -> bool:
        idx = bisect.bisect(self.intervals, [left, int(1e9)])
        if not self.intervals or idx == 0:
            return False
        return self.intervals[idx-1][1] >= right

    def removeRange(self, left: int, right: int) -> None:
        ret = []
        for interval in self.intervals:
            if left <= interval[0] and right >= interval[1]:
                continue
            elif left >= interval[1] or right <= interval[0]:
                ret.append(interval)
            elif left < interval[0]:
                ret.append([right, interval[1]])
            elif right > interval[1]:
                ret.append([interval[0], left])
            else:
                ret.append([interval[0], left])
                ret.append([right, interval[1]])
        self.intervals = ret


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
