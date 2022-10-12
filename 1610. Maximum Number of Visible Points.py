from math import atan2, pi
from bisect import bisect_right
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:   
        numLoc = 0
        angles = []
        for point in points:
            x, y = point[0] - location[0], point[1] - location[1]
            if x == 0 and y == 0:
                numLoc += 1
            else:
                val = atan2(y, x) * 180 / pi
                if val < 0:
                    val += 360
                angles.append(val)
        angles.sort()
        angles += [angle+360 for angle in angles]
        
        ret = numLoc
        for i in range(len(angles)//2):
            j = bisect_right(angles, angles[i]+angle)
            ret = max(ret, j - i + numLoc)
        return ret
