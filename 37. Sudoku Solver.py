class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        num_left = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    num_left += 1
        self.solver(board, num_left)     
        
        
    def solver(self, board, num_left):
        if num_left == 0:
            return True
        
        # Search Blank -> (i, j)
        start_y, start_x = 0, 0
        found_flag = False
        for t in range(1, 10):
            for i in range(start_y, start_y+3):
                for j in range(start_x, start_x+3):
                    if board[i][j] == '.':
                        found_flag = True
                        break
                if found_flag:
                    break
            if found_flag:
                break
            start_x += 3
            if t % 3 == 0:
                start_y += 3
                start_x = 0
                
        candidates = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        excludes = set()
        
        # Square
        start_y, start_x = i // 3 * 3, j // 3 * 3
        for y in range(start_y, start_y+3):
            for x in range(start_x, start_x+3):
                if board[y][x] != '.':
                    excludes.add(board[y][x])
                
        # Horizontal
        for x in range(9):
            if board[i][x] != '.':
                excludes.add(board[i][x])
        
        # Vertical
        for y in range(9):
            if board[y][j] != '.':
                excludes.add(board[y][j])
        
        candidates = [candidate for candidate in candidates \
                      if candidate not in list(excludes)]
        
        for num in candidates:
            board[i][j] = num
            if self.solver(board, num_left - 1):
                return True
        board[i][j] = '.'
        return False

        
