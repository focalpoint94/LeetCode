'''
Dijkstra
'''

import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        # (dist_u, y, x)
        h = [(0, 0, 0)]
        visited = set()
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
        while h:
            dist_u, y, x = heapq.heappop(h)
            if (y, x) in visited:
                continue
            visited.add((y, x))
            # arrived!
            if (y, x) == (m-1, n-1):
                return dist_u
            for d in range(4):
                next_y, next_x = y + dy[d], x + dx[d]
                if 0 <= next_y < m and 0 <= next_x < n:
                    if (next_y, next_x) not in visited:
                        dist_v = max(dist_u, abs(heights[next_y][next_x]-heights[y][x]))
                        heapq.heappush(h, (dist_v, next_y, next_x))

'''
Binary Search
'''

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        
        def isReachable(budget):
            visited = set()
            visited.add((0, 0))
            q = [(0, 0)]
            dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
            while q:
                next_q = []
                for y, x in q:
                    for d in range(4):
                        next_y, next_x = y + dy[d], x + dx[d]
                        if 0 <= next_y < m and 0 <= next_x < n:
                            if (next_y, next_x) not in visited:
                                cost = abs(heights[next_y][next_x]-heights[y][x])
                                if cost <= budget:
                                    visited.add((next_y, next_x))
                                    next_q.append((next_y, next_x))
                q = next_q
            return (m-1, n-1) in visited
        
        ret = 10 ** 6
        left, right = 0, 10**6
        while left <= right:
            mid = (left + right) // 2
            if isReachable(mid):
                ret = min(ret, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ret

'''
BFS
'''

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = 0
        q = [(0, 0, 0)]
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
        while q:
            next_q = []
            for y, x, c in q:
                if dp[y][x] == c:
                    for d in range(4):
                        next_y, next_x = y + dy[d], x + dx[d]
                        if 0 <= next_y < m and 0 <= next_x < n:
                            cost = max(c, abs(heights[y][x]-heights[next_y][next_x]))
                            if cost < dp[next_y][next_x]:
                                dp[next_y][next_x] = cost
                                next_q.append((next_y, next_x, cost))
            q = next_q
        return dp[-1][-1]
