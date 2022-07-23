from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
        
        def bfs(y, x):
            nonlocal m, n, dy, dx
            ret = 0
            q = deque()
            q.append((y, x))
            grid[y][x] = -1
            while q:
                y, x = q.popleft()
                ret += 1
                for d in range(4):
                    next_y, next_x = y + dy[d], x + dx[d]
                    if 0 <= next_y < m and 0 <= next_x < n:
                        if grid[next_y][next_x] == 1:
                            q.append((next_y, next_x))
                            grid[next_y][next_x] = -1
            return ret
        
        ret = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    ret = max(ret, bfs(y, x))
        return ret
