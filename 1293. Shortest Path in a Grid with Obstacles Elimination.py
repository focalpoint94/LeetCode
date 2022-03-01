class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid) - 1, len(grid[0]) - 1
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
        q = set()
        q.add((0, 0, k))
        dp = {}
        dp[(0, 0)] = 0
        step = 0
        while q:
            next_q = set()
            for y, x, i in q:
                # if reached the goal:
                if y == m and x == n:
                    return step
                for d in range(4):
                    next_y, next_x = y + dy[d], x + dx[d]
                    # if next point is valid:
                    if 0 <= next_y <= m and 0 <= next_x <= n:
                        # if next point is empty:
                        if grid[next_y][next_x] == 0:
                            # if next point is not visited or it is efficient:
                            if (next_y, next_x) not in dp or \
                                i > dp[(next_y, next_x)]:
                                dp[(next_y, next_x)] = i
                                next_q.add((next_y, next_x, i))
                        # if next point is wall:
                        else:
                            # if next point is not visited or it is efficient:
                            if (next_y, next_x) not in dp or \
                                i - 1 > dp[(next_y, next_x)]:
                                if i >= 1:
                                    dp[(next_y, next_x)] = i - 1
                                    next_q.add((next_y, next_x, i-1))
            q = next_q
            step += 1
        return -1
