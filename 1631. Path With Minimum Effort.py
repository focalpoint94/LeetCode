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
