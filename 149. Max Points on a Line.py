from collections import defaultdict
import math
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ret = 1
        for i in range(len(points)):
            p1 = points[i]
            lineDict = defaultdict(lambda: 1)
            for j in range(len(points)):
                if i == j:
                    continue
                p2 = points[j]
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]
                if dx == 0:
                    slope = (0, 1)
                elif dy == 0:
                    slope = (1, 0)
                else:
                    gcd = math.gcd(dy, dx)
                    slope = (dx // gcd, dy // gcd)
                lineDict[slope] += 1
                ret = max(ret, lineDict[slope])
        return ret
