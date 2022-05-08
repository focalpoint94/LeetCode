import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = [(grid[0][0], 0, 0)]
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
        visited = set()
        visited.add((0, 0))
        while q:
            time, y, x = heapq.heappop(q)
            if y == m-1 and x == n-1:
                return time
            for d in range(4):
                nextY, nextX = y + dy[d], x + dx[d]
                if 0 <= nextY < m and 0 <= nextX < n:
                    if (nextY, nextX) not in visited:
                        heapq.heappush(q, (max(time, grid[nextY][nextX]), nextY, nextX))
                        visited.add((nextY, nextX))
