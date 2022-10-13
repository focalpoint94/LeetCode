from bisect import bisect_left, bisect_right
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        self.ranges = []
        ret = []
        for left, right in paint:
            ret.append(self.insertRange(left, right))
        return ret
        
    def insertRange(self, left, right):
        start = bisect_left(self.ranges, left)
        end = bisect_right(self.ranges, right)
        
        blocks = []
        # calculate newly painted area & update range
        if start % 2 == 0 and end % 2 == 0:
            # for calculation
            blocks.append(left)
            blocks += self.ranges[start:end]
            blocks.append(right)
            # for update
            self.ranges[start:end] = [left, right]
        elif start % 2 == 1 and end % 2 == 0:
            # for calculation
            blocks += self.ranges[start:end]
            blocks.append(right)
            # for update
            self.ranges[start:end] = [right]
        elif start % 2 == 0 and end % 2 == 1:
            # for calculation
            blocks.append(left)
            blocks += self.ranges[start:end]
            # for update
            self.ranges[start:end] = [left]
        else:
            # for calculation
            blocks += self.ranges[start:end]
            # for update
            self.ranges[start:end] = []
            
        ret = 0
        for i in range(1, len(blocks), 2):
            ret += blocks[i] - blocks[i-1]
        return ret
        
#         residuals = []
#         new_range = []
        
#         if start % 2 == 0:
#             new_range.append(left)
#             residuals.append(left)
#         residuals += self.ranges[start:end]
#         if end % 2 == 0:
#             new_range.append(right)
#             residuals.append(right)
#         self.ranges[start:end] = new_range
        
#         ret = 0
#         for i in range(1, len(residuals), 2):
#             ret += residuals[i] - residuals[i-1]
#         return ret
