from functools import cmp_to_key
import heapq

class MyHeap:
    def __init__(self, type='min'):
        self.heap = []
        self.removals = []
        self.sign = 1 if type == 'min' else -1

    def insert(self, elem):
        heapq.heappush(self.heap, self.sign * elem)

    def __getitem__(self, idx):
        return self.sign * self.heap[idx]

    def __len__(self):
        return len(self.heap) - len(self.removals)

    def remove(self, elem):
        if elem == self.sign * self.heap[0]:
            heapq.heappop(self.heap)
            while self.removals and self.heap[0] == self.removals[0]:
                heapq.heappop(self.heap)
                heapq.heappop(self.removals)
        else:
            heapq.heappush(self.removals, self.sign * elem)

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for x, y, h in buildings:
            points.append((x, h, 0))
            points.append((y, h, 1))
        
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
        q = MyHeap(type='max')
        q.insert(0)
        for x, h, t in points:
            prevH = q[0]
            if t == 0:
                q.insert(h)
                if q[0] != prevH:
                    ret.append((x, h))
            else:
                q.remove(h)
                if q[0] != prevH:
                    ret.append((x, q[0]))
        return ret




# from functools import cmp_to_key
# import heapq

# class PriorityQueue:
#     def __init__(self):
#         self.pq = []
#         self.removals = []

#     def insert(self, elem):
#         heapq.heappush(self.pq, -elem)

#     def getmax(self):
#         return -self.pq[0]

#     def remove(self, elem):
#         if elem == -self.pq[0]:
#             heapq.heappop(self.pq)
#             while self.removals and self.pq[0] == self.removals[0]:
#                 heapq.heappop(self.pq)
#                 heapq.heappop(self.removals)
#         else:
#             heapq.heappush(self.removals, -elem)

# class Solution:
#     def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
#         # [loc, height, isEnd]
#         points = []
#         for l, r, h in buildings:
#             points.append([l, h, 0])
#             points.append([r, h, 1])
        
#         def compare(p1, p2):
#             if p1[0] != p2[0]:
#                 return p1[0] - p2[0]
#             if p1[2] != p2[2]:
#                 return p1[2] - p2[2]
#             if p1[2] == 0:
#                 return -(p1[1] - p2[1])
#             return p1[1] - p2[1]
            
#         points.sort(key=cmp_to_key(compare))
        
#         ret = []
#         pq = PriorityQueue()
#         pq.insert(0)
#         for loc, height, isEnd in points:
#             prevmax = pq.getmax()
#             if not isEnd:
#                 pq.insert(height)
#                 if pq.getmax() != prevmax:
#                     ret.append([loc, height])
#             else:
#                 pq.remove(height)
#                 if pq.getmax() != prevmax:
#                     ret.append([loc, pq.getmax()])
#         return ret
