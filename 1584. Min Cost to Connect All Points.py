class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parents = [i for i in range(n)]
        
        def find_parent(p1):
            if parents[p1] == p1:
                return p1
            parents[p1] = find_parent(parents[p1])
            return parents[p1]
        
        def union_parent(p1, p2):
            p1 = find_parent(p1)
            p2 = find_parent(p2)
            if p1 < p2:
                parents[p2] = p1
            else:
                parents[p1] = p2
        
        ret = 0
        import heapq
        h = []
        for i, p1 in enumerate(points):
            for j in range(i+1, len(points)):
                p2 = points[j]
                d = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
                heapq.heappush(h, (d, i, j))
        
        while h:
            d, u, v = heapq.heappop(h)
            if find_parent(u) != find_parent(v):
                ret += d
                union_parent(u, v)
        return ret
