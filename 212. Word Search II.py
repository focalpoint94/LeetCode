class Solution:
    def findWords(self, board, words):
        self.ret = []
        self.trie = {}
        for word in words:
            t = self.trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'
        
        m, n = len(board), len(board[0])
        for y in range(m):
            for x in range(n):
                self.dfs(board, self.trie, y, x, '')
        return self.ret
    
    def dfs(self, board, node, y, x, word):
        if '#' in node:
            del node['#']
            self.ret.append(word)
        
        if 0 > y or y >= len(board) or 0 > x or x >= len(board[0]):
            return
        
        char = board[y][x]
        if char not in node:
            return
        
        next_node = node[char]
        board[y][x] = '@'
        dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
        for d in range(4):
            next_y, next_x = y + dy[d], x + dx[d]
            self.dfs(board, next_node, next_y, next_x, word+char)
        board[y][x] = char
        if not next_node:
            del node[char]
