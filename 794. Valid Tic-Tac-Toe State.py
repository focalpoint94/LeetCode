class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        n1, n2 = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    n1 += 1
                elif board[i][j] == 'O':
                    n2 += 1
        if n1 != n2 and n1 != n2 + 1:
            return False
        states = []
        for i in range(3):
            states.append(board[i])
        for j in range(3):
            states.append(''.join([board[i][j] for i in range(3)]))
        states.append(board[0][0]+board[1][1]+board[2][2])
        states.append(board[0][2]+board[1][1]+board[2][0])
        
        if "XXX" in states and "OOO" in states:
            return False
        if "XXX" in states and n1 == n2:
            return False
        if "OOO" in states and n1 == n2 + 1:
            return False
        return True
