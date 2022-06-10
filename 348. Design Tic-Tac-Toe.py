class TicTacToe:
    
    def __init__(self, n: int):
        self.rows, self.cols = [0] * n, [0] * n
        self.diag = [0] * 2
        self.n = n
    
    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.rows[row] += 1
            self.cols[col] += 1
            if row == col:
                self.diag[0] += 1
            if row + col == self.n - 1:
                self.diag[1] += 1
            if self.rows[row] == self.n or self.cols[col] == self.n or \
            self.diag[0] == self.n or self.diag[1] == self.n:
                return 1
        else:
            self.rows[row] -= 1
            self.cols[col] -= 1
            if row == col:
                self.diag[0] -= 1
            if row + col == self.n - 1:
                self.diag[1] -= 1
            if self.rows[row] == -self.n or self.cols[col] == -self.n or \
            self.diag[0] == -self.n or self.diag[1] == -self.n:
                return 2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
