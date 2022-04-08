import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        boundaries = []
        for i in range(n):
            boundaries.append((0, i))
            boundaries.append((m - 1, i))
        for i in range(1, m - 1):
            boundaries.append((i, 0))
            boundaries.append((i, n - 1))

        # heights: min heap of boundaries
        # if popped, will return min height of the current boundaries
        heights = []
        for y, x in boundaries:
            heapq.heappush(heights, (heightMap[y][x], y, x))

        visited = set()
        visited.update(boundaries)

        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

        ret = 0

        while heights:
            h, y, x = heapq.heappop(heights)
            for d in range(4):
                next_y, next_x = y + dy[d], x + dx[d]
                if 0 <= next_y < m and 0 <= next_x < n and (next_y, next_x) not in visited:
                    visited.add((next_y, next_x))
                    if heightMap[next_y][next_x] <= h:
                        ret += h - heightMap[next_y][next_x]
                        heapq.heappush(heights, (h, next_y, next_x))
                    else:
                        heapq.heappush(heights, (heightMap[next_y][next_x], next_y, next_x))
        return ret    
