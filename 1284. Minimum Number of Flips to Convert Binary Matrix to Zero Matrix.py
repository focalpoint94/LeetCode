class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        self.mat = mat
        m, n = len(self.mat), len(self.mat[0])
        buttons = [i for i in range(m*n)]
        self.ret = 10
        self.dfs(buttons, [])
        return self.ret if self.ret != 10 else -1
        
    def dfs(self, buttons, visited):
        if self.isComplete():
            self.ret = min(self.ret, len(visited))
            return
        for i, button in enumerate(buttons):
            self.push(button)
            self.dfs(buttons[i+1:], visited+[button])
            self.push(button)
        
    def isComplete(self):
        m, n = len(self.mat), len(self.mat[0])
        for y in range(m):
            for x in range(n):
                if self.mat[y][x] != 0:
                    return False
        return True
    
    def push(self, button):
        m, n = len(self.mat), len(self.mat[0])
        y, x = button // n, button - button // n * n
        self.mat[y][x] ^= 1
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
        for d in range(4):
            next_y, next_x = y + dy[d], x + dx[d]
            if 0 <= next_y < m and 0 <= next_x < n:
                self.mat[next_y][next_x] ^= 1
        
