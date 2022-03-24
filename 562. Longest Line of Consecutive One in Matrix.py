class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        self.mat = mat
        self.dp = [[[0] * 8 for col in range(n)] for row in range(m)]
        self.ret = 0
        
        dys, dxs = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
        for y in range(m):
            for x in range(n):
                for d in range(8):
                    dy, dx = dys[d], dxs[d]
                    if self.mat[y][x] == 1 and not self.dp[y][x][d]:
                        self.dfs(y, x, d, dy, dx)
        return self.ret
        
    def dfs(self, y, x, d, dy, dx):
        if y < 0 or y >= len(self.mat) or x < 0 or x >= len(self.mat[0]) or \
            self.mat[y][x] == 0:
            return 0
        
        if self.dp[y][x][d] != 0:
            return self.dp[y][x][d]
        
        next_y, next_x = y + dy, x + dx
        ret = self.dfs(next_y, next_x, d, dy, dx) + 1
        self.dp[y][x][d] = ret
        self.ret = max(self.ret, ret)
        return ret
