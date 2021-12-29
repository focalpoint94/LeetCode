class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for y in range(m):
            for x in range(n):
                cnt = self.countOnes(board, y, x)
                if board[y][x] == 0:
                    if cnt == 3:
                        board[y][x] = 3
                else:
                    if cnt != 2 and cnt != 3:
                        board[y][x] = 2
        for y in range(m):
            for x in range(n):
                if board[y][x] == 3:
                    board[y][x] = 1
                elif board[y][x] == 2:
                    board[y][x] = 0
        
    def countOnes(self, board, y, x):
        dy = [-1, -1, 0, 1, 1, 1, 0, -1]
        dx = [0, 1, 1, 1, 0, -1, -1, -1]
        cnt = 0
        for d in range(8):
            next_y, next_x = y + dy[d], x + dx[d]
            if 0 <= next_y <= len(board) - 1 and 0 <= next_x <= len(board[0]) - 1:
                if board[next_y][next_x] == 1 or board[next_y][next_x] == 2:
                    cnt += 1
        return cnt
