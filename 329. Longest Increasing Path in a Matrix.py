class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.visited = [[False] * n for _ in range(m)]
        self.dp = [[-1] * n for _ in range(m)]
        ret = 0
        for y in range(m):
            for x in range(n):
                if not self.visited[y][x]:
                    ret = max(ret, self.dfs(y, x))
        return ret
        
    def dfs(self, y, x):
        if self.visited[y][x]:
            return self.dp[y][x]
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        
        self.visited[y][x] = True
        self.dp[y][x] = 1
        for d in range(4):
            next_y, next_x = y + dy[d], x + dx[d]
            if 0 <= next_y < len(self.matrix) and 0 <= next_x < len(self.matrix[0]):
                if self.matrix[next_y][next_x] > self.matrix[y][x]:
                    self.dp[y][x] = max(self.dp[y][x], self.dfs(next_y, next_x) + 1)
        return self.dp[y][x]
