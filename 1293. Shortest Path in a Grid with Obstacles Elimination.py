from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
        
        q = deque()
        q.append((0, 0, k, 0))
        
        visited = {}
        # point: t
        visited[(0, 0)] = k
        
        while q:
            y, x, t, l = q.popleft()
            # arrived
            if y == m - 1 and x == n - 1:
                return l
            for d in range(4):
                next_y, next_x = y + dy[d], x + dx[d]
                # within grid
                if 0 <= next_y < m and 0 <= next_x < n:
                    # never visited
                    if (next_y, next_x) not in visited:
                        visited[(next_y, next_x)] = t
                        # empty
                        if grid[next_y][next_x] == 0:
                            q.append((next_y, next_x, t, l+1))
                        else:
                            if t >= 1:
                                q.append((next_y, next_x, t-1, l+1))
                    # if visited
                    else:
                        if t > visited[(next_y, next_x)]:
                            visited[(next_y, next_x)] = t
                            # empty
                            if grid[next_y][next_x] == 0:
                                q.append((next_y, next_x, t, l+1))
                            else:
                                if t >= 1:
                                    q.append((next_y, next_x, t-1, l+1))
        return -1
        
