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
                        cost = max(dist_u, abs(heights[next_y][next_x]-heights[y][x]))
                        heapq.heappush(h, (cost, next_y, next_x))
