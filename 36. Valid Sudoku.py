class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    # 가로
                    for k in range(9):
                        if k == j:
                            continue
                        if board[i][j] == board[i][k]:
                            return False
                    # 세로
                    for k in range(9):
                        if k == i:
                            continue
                        if board[i][j] == board[k][j]:
                            return False
                    # 사각형
                    start_y = i // 3 * 3
                    start_x = j // 3 * 3
                    for y in range(start_y, start_y+3):
                        for x in range(start_x, start_x + 3):
                            if y == i or x == j:
                                continue
                            if board[i][j] == board[y][x]:
                                return False
        return True
        
        
        
