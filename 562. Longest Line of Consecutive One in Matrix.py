from functools import lru_cache
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = {}
        for y in range(m):
            for x in range(n):
                dp[(y, x)] = [False] * 8
        
        ret = 0
        dy, dx = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
        
        def dfs(y, x, d):
            nonlocal m, n, ret
            if dp[(y, x)][d] != False:
                return dp[(y, x)][d]
            
            if mat[y][x] == 0:
                dp[(y, x)][d] = 0
                return 0
            
            next_y, next_x = y + dy[d], x + dx[d]
            if 0 <= next_y < m and 0 <= next_x < n:
                dp[(y, x)][d] = dfs(next_y, next_x, d) + 1
            else:
                dp[(y, x)][d] = 1
            ret = max(ret, dp[(y, x)][d])
            return dp[(y, x)][d]
            
        for y in range(m):
            for x in range(n):
                for d in range(8):
                    dfs(y, x, d)
                    
        return ret
