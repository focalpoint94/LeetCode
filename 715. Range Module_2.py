from bisect import bisect_left, bisect_right
class RangeModule:

    def __init__(self):
        self.range = []
        
    def addRange(self, left: int, right: int) -> None:
        start = bisect_left(self.range, left)
        end = bisect_right(self.range, right)
        newRange = []
        if start % 2 == 0:
            newRange.append(left)
        if end % 2 == 0:
            newRange.append(right)
        self.range[start:end] = newRange
        
    def queryRange(self, left: int, right: int) -> bool:
        start = bisect_right(self.range, left)
        end = bisect_left(self.range, right)
        return start == end and start % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        start = bisect_left(self.range, left)
        end = bisect_right(self.range, right)
        newRange = []
        if start % 2 == 1:
            newRange.append(left)
        if end % 2 == 1:
            newRange.append(right)
        self.range[start:end] = newRange

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
