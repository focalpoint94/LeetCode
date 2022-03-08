class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        import heapq
        boundaries = []
        m, n = len(heightMap), len(heightMap[0])
        
        visited = [[False] * n for _ in range(m)]
        for y in range(m):
            for x in range(n):
                if y == 0 or y == m - 1 or x == 0 or x == n - 1:
                    heapq.heappush(boundaries, (heightMap[y][x], y, x))
                    visited[y][x] = True
        
        ret = 0
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
        while boundaries:
            h, y, x = heapq.heappop(boundaries)    
            for d in range(4):
                next_y, next_x = y + dy[d], x + dx[d]
                if 0 <= next_y < m and 0 <= next_x < n and not visited[next_y][next_x]:
                    if heightMap[next_y][next_x] >= h:
                        heapq.heappush(boundaries, (heightMap[next_y][next_x], next_y, next_x))
                    else:
                        ret += h - heightMap[next_y][next_x]
                        heapq.heappush(boundaries, (h, next_y, next_x))
                    visited[next_y][next_x] = True            
        return ret
