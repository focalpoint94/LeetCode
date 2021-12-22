from functools import cmp_to_key
import heapq

class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.removals = []

    def insert(self, elem):
        heapq.heappush(self.pq, -elem)

    def getmax(self):
        return -self.pq[0]

    def remove(self, elem):
        if elem == -self.pq[0]:
            heapq.heappop(self.pq)
            while self.removals and self.pq[0] == self.removals[0]:
                heapq.heappop(self.pq)
                heapq.heappop(self.removals)
        else:
            heapq.heappush(self.removals, -elem)

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
        pq = PriorityQueue()
        pq.insert(0)
        for loc, height, isEnd in points:
            prevmax = pq.getmax()
            if not isEnd:
                pq.insert(height)
                if pq.getmax() != prevmax:
                    ret.append([loc, height])
            else:
                pq.remove(height)
                if pq.getmax() != prevmax:
                    ret.append([loc, pq.getmax()])
        return ret
        
