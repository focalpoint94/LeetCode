from functools import cmp_to_key
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # [loc, height, isEnd]
        points = []
        for l, r, h in buildings:
            points.append([l, h, 0])
            points.append([r, h, 1])
        
        def compare(p1, p2):
            if p1[0] != p2[0]:
                return p1[0] - p2[0]
            if p1[2] != p2[2]:
                return p1[2] - p2[2]
            if p1[2] == 0:
                return -(p1[1] - p2[1])
            return p1[1] - p2[1]
            
        points.sort(key=cmp_to_key(compare))
        
        ret = []
        pq = [0]
        for loc, height, isEnd in points:
            prevmax = -pq[0]
            if not isEnd:
                heapq.heappush(pq, -height)
                if -pq[0] != prevmax:
                    ret.append([loc, height])
            else:
                pq.remove(-height)
                heapq.heapify(pq)
                if -pq[0] != prevmax:
                    ret.append([loc, -pq[0]])
        return ret
        
