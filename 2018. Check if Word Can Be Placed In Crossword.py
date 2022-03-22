class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        k = len(word)
        self.board = board
        self.word = word
        self.visited = [[False] * n for _ in range(m)]
        startings = []
        
        # horizontal search
        for y in range(m):
            for x in range(n):
                if self.board[y][x] != '#' and not self.visited[y][x]:
                    if self.dfs(y, x, 'horizontal') == k:
                        startings.append((y, x, 'right'))
                        startings.append((y, x+k-1, 'left'))
        
        self.visited = [[False] * n for _ in range(m)]
        
        # vertical search
        for y in range(m):
            for x in range(n):
                if self.board[y][x] != '#' and not self.visited[y][x]:
                    if self.dfs(y, x, 'vertical') == k:
                        startings.append((y, x, 'down'))
                        startings.append((y+k-1, x, 'up'))
        
        for y, x, direction in startings:
            if self.isMatch(0, y, x, direction):
                return True
        return False
                        
                    
    def dfs(self, y, x, direction):
        m, n = len(self.board), len(self.board[0])
        if y < 0 or y >= m or x < 0 or x >= n or self.board[y][x] == '#':
            return 0
        if direction == 'horizontal':
            dy, dx = 0, 1
        else:
            dy, dx = 1, 0
        next_y, next_x = y + dy, x + dx
        ret = self.dfs(next_y, next_x, direction) + 1
        self.visited[y][x] = True
        return ret
    
    
    def isMatch(self, word_idx, y, x, direction):
        if word_idx == len(self.word):
            return True
        if self.board[y][x] != ' ' and self.board[y][x] != self.word[word_idx]:
            return False
        if direction == 'right':
            dy, dx = 0, 1
        elif direction == 'left':
            dy, dx = 0, -1
        elif direction == 'down':
            dy, dx = 1, 0
        else:
            dy, dx = -1, 0
        next_y, next_x = y + dy, x + dx
        return self.isMatch(word_idx+1, next_y, next_x, direction)
        
        
