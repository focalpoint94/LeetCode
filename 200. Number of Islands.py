class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m, self.n = len(self.grid), len(self.grid[0])
        self.visited = [[False] * self.n for _ in range(self.m)]
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        ret = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == '1' and not self.visited[i][j]:
                    self.dfs(i, j, dy, dx)
                    ret += 1
        return ret  
        
    def dfs(self, y, x, dy, dx):
        self.visited[y][x] = True
        for t in range(4):
            next_y = y + dy[t]
            next_x = x + dx[t]
            if 0 <= next_y <= self.m - 1 and 0 <= next_x <= self.n - 1:
                if self.grid[next_y][next_x] == '1' and not self.visited[next_y][next_x]:
                    self.dfs(next_y, next_x, dy, dx)
