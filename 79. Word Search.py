class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False
    
    def dfs(self, board, y, x, word, k):
        if k == len(word):
            return True
        if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]) or board[y][x] == '@':
            return False
        char = word[k]
        if board[y][x] != char:
            return False
        board[y][x] = '@'
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
        for d in range(4):
            next_y, next_x = y + dy[d], x + dx[d]
            if self.dfs(board, next_y, next_x, word, k+1):
                return True
        board[y][x] = char
        return False
