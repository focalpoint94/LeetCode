class RangeModule:
    from bisect import bisect_left, bisect_right
    
    def __init__(self):
        self.range = []
    
    def addRange(self, left: int, right: int) -> None:
        start = bisect_left(self.range, left)
        end = bisect_right(self.range, right)
        
        new_range = []
        if start % 2 == 0:
            new_range.append(left)
        if end % 2 == 0:
            new_range.append(right)
        self.range[start:end] = new_range
        
    def queryRange(self, left: int, right: int) -> bool:
        start = bisect_right(self.range, left)
        end = bisect_left(self.range, right)
        return start == end and start % 2 == 1
    
    def removeRange(self, left: int, right: int) -> None:
        start = bisect_left(self.range, left)
        end = bisect_right(self.range, right)
        
        new_range = []
        if start % 2 == 1:
            new_range.append(left)
        if end % 2 == 1:
            new_range.append(right)
        self.range[start:end] = new_range


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
