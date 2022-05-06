class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ret = 0
        for y in range(m):
            for x in range(n):
                if board[y][x] == 'X' and (y == 0 or board[y-1][x] == '.') and (x==0 or board[y][x-1] == '.'):
                    ret += 1
        return ret
