class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
        
        visited = set()
        
        def dfs(y, x):
            grid[y][x] = '2'
            visited.add((y, x))
            for d in range(4):
                next_y, next_x = y + dy[d], x + dx[d]
                if 0 <= next_y < m and 0 <= next_x < n:
                    if grid[next_y][next_x] == '1':
                        if (next_y, next_x) not in visited:
                            dfs(next_y, next_x)
        
        ret = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1':
                    dfs(y, x)
                    ret += 1
        return ret
